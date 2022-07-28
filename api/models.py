from django.db import models

 
class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Transaction(models.Model):
    DEBIT = 'DEBIT' # Money into account
    CREDIT = 'CREDIT' # Money out of the account
    action_choices = [
        (DEBIT, 'DEBIT'),
        (CREDIT, 'CREDIT'),
    ]

    action = models.CharField(max_length=10, choices=action_choices, default=DEBIT)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
