from rest_framework import status

from api.models import Account
from api.tests import BaseAPITestCase


class TransferTestCase(BaseAPITestCase):

    def test_transfer_to_account(self):
        account = Account.objects.create(
            customer=self.customer2,
            balance=100.00
        )
        sender_account = Account.objects.create(
            customer=self.customer1,
            balance=1000.00
        )
        data = {
            "customer": self.customer1.id,
            "sender_account": sender_account.id,
            "recipient_account": account.id,
            "amount": 100.00
        }
        response = self.client.post('/api/v1/transfers/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Reload  receipt account to confirm account has been debited
        self.assertEqual(Account.objects.get(pk=account.id).balance, 200.00)
        # Reload  receipt account to confirm account has been credited
        self.assertEqual(Account.objects.get(pk=sender_account.id).balance, 900.00)

    def test_transfer_with_insufficient_balance(self):
        sender_account = Account.objects.create(
            customer=self.customer1,
            balance=1000.00
        )
        data = {
            "customer": self.customer1.id,
            "sender_account": sender_account.id,
            "recipient_account": self.account2.id,
            "amount": 1100.00,
        }
        response = self.client.post('/api/v1/transfers/', data=data)
        self.assertIn('Insufficient account balance 1000.00!', response.data['non_field_errors'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transfer_with_invalid_sender_account(self):
        data = {
            "customer": self.customer1.id,
            "sender_account": 340987,
            "recipient_account": self.account2.id,
            "amount": 1100.00,
        }
        response = self.client.post('/api/v1/transfers/', data=data)
        self.assertIn('Invalid sender account!', response.data['non_field_errors'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transfer_with_invalid_receipient_account(self):
        data = {
            "customer": self.customer1.id,
            "sender_account": self.account1.id,
            "recipient_account": 537227,
            "amount": 1100.00,
        }
        response = self.client.post('/api/v1/transfers/', data=data)
        self.assertIn('Invalid recipient account!', response.data['recipient_account'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
