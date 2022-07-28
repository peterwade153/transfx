from rest_framework import status

from api.tests import BaseAPITestCase


class AccountCreateTestCase(BaseAPITestCase):

    def test_create_account(self):
        data = {
            "customer": self.customer1.id,
            "balance": 1000.34
        }
        response = self.client.post('/api/v1/accounts/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_multiple_accounts_for_customer(self):
        data = {"customer": self.customer1.id, "balance": 1000.34}
        response = self.client.post('/api/v1/accounts/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        resp = self.client.post('/api/v1/accounts/', data=data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_create_account_with_zero_balance(self):
        data = {
            "customer": self.customer1.id,
            "balance": 0.00
        }
        response = self.client.post('/api/v1/accounts/', data=data)
        self.assertIn('Balance amount should be greater than zero', response.data['balance'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_account_for_unkwown_customer(self):
        data = {
            "customer": 234,
            "balance": 12.00
        }
        response = self.client.post('/api/v1/accounts/', data=data)
        self.assertIn('Invalid pk "234" - object does not exist.', response.data['customer'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
