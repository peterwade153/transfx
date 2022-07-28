from rest_framework import status

from api.models import Account
from api.tests import BaseAPITestCase


class AccountBalanceRetrieveTestCase(BaseAPITestCase):

    def test_list_account_balance(self):
        account = Account.objects.create(
            customer=self.customer2,
            balance=100.00
        )
        response = self.client.get(f'/api/v1/account-balance/{account.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], '100.00')

    def test_list_account_balance_invalid_account(self):
        response = self.client.get(f'/api/v1/account-balance/{15563}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
