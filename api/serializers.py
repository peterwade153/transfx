from django.db import transaction
from rest_framework import serializers

from api.models import Account, Transaction
from api.account_utils.account_update import update_account_balance


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        read_only_fields = ['id']
        fields = read_only_fields + ['customer', 'balance']

        extra_kwargs = {'customer': {'required': True}}
        extra_kwargs = {'balance': {'required': True}}

    def validate_balance(self, value):
        if value <= 0:
            raise serializers.ValidationError('Balance amount should be greater than zero')
        return value

    def create(self, validated_data):
        with transaction.atomic():
            account = Account.objects.create(**validated_data)
            # Add transaction for the new account balance
            Transaction.objects.create(
                account=account,
                action=Transaction.DEBIT,
                customer=validated_data['customer'],
                completed=True
            )
            return account


class TransferSerializer(serializers.Serializer):
    customer = serializers.IntegerField()
    sender_account = serializers.IntegerField()
    recipient_account = serializers.IntegerField()
    amount = serializers.DecimalField(decimal_places=2, min_value=0.00, max_digits=15)
    
    def validate_recipient_account(self, value):
        try:
            Account.objects.get(pk=value)
        except Account.DoesNotExist:
            raise serializers.ValidationError('Invalid recipient account!')
        return value

    def validate(self, attrs):
        try:
            account = Account.objects.get(
                customer_id=attrs['customer'],
                pk=attrs['sender_account']
            )
            if account.balance < attrs['amount']:
                raise serializers.ValidationError(f'Insufficient account balance {account.balance}!')
        except Account.DoesNotExist:
            raise serializers.ValidationError('Invalid sender account!')
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
        # credit sender account
            Transaction.objects.create(
                account_id=validated_data['sender_account'],
                action=Transaction.CREDIT,
                customer_id=validated_data['customer'],
                completed=True
            )
            # debit recipient account
            Transaction.objects.create(
                account_id=validated_data['recipient_account'],
                action=Transaction.DEBIT,
                customer_id=validated_data['customer'],
                completed=True
            )
            # Credit sender account
            update_account_balance(
                validated_data['sender_account'],
                validated_data['amount'],
                Transaction.CREDIT
            )
            # Debit reciever account
            update_account_balance(
                validated_data['recipient_account'],
                validated_data['amount'],
                Transaction.DEBIT
            )
        return validated_data


class AccountBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['balance', ]


class TrasanctionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['action', 'account', 'customer', 'completed']


class AccountTransactionsSerializer(serializers.ModelSerializer):
    transactions = TrasanctionsSerializer(many=True)

    class Meta:
        model = Account
        fields = ['transactions', ]
