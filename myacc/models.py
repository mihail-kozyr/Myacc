from datetime import datetime

from django.db import models

#TODO: create model Contractor
class Contractor(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=512)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    index = models.IntegerField()
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    comment = models.TextField(max_length=4000)

#TODO: create model Account
class Account(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    accno = models.CharField(max_length=30)
    initial_balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=2, decimal_places=2)
    is_closed = models.BooleanField()
    comment = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE)
    comment = models.TextField()


#TODO: create model Transaction
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateField(default=datetime.now)
    transaction_type = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    comment = models.TextField()