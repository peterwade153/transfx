from rest_framework import status

from api.models import Account, Transaction
from api.tests import BaseAPITestCase


class AccountBalanceRetrieveTestCase(BaseAPITestCase):

    def test_list_account_balance(self):
        account = Account.objects.create(
            customer=self.customer2,
            balance=100.00
        )
        Transaction.objects.create(
            account=account,
            customer=self.customer2,
            action=Transaction.DEBIT,
            completed=True
        )
        Transaction.objects.create(
            account=account,
            customer=self.customer1,
            action=Transaction.CREDIT,
            completed=True
        )
        response = self.client.get(f'/api/v1/account-transactions/{account.id}/', format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
