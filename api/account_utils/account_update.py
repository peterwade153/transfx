from django.db.models import F

from api.models import Account, Transaction


def update_account_balance(account, amount, action):
    account = Account.objects.get(pk=account)
    if action == Transaction.DEBIT:
        account.balance = F('balance') + amount
    elif action == Transaction.CREDIT:
        account.balance = F('balance') - amount
    account.save()
    return
