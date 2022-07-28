from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import Account, Transaction
from api import serializers


class AccountView(GenericViewSet, CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


class TransferView(GenericViewSet, CreateModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransferSerializer


class AccountBalanceView(GenericViewSet, RetrieveModelMixin):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountBalanceSerializer


class AccountTransactionsView(GenericViewSet, RetrieveModelMixin):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountTransactionsSerializer

