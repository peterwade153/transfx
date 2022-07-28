from rest_framework.test import APITestCase

from api.models import Account, Customer, Transaction


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.customer1 = Customer.objects.create(
            name="Branden Gibson"
        )
        self.customer2 = Customer.objects.create(
            name="Arisha Barron"
        )
        self.customer3 = Customer.objects.create(
            name="Georgina Hazel"
        )
        self.account1 = Account.objects.create(
            customer=self.customer1,
            balance=10000.00
        )
        self.account2 = Account.objects.create(
            customer=self.customer1,
            balance=100.00
        )
        self.account3 = Account.objects.create(
            customer=self.customer2,
            balance=100.00
        )

