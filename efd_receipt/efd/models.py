from django.db import models


class Taxpayer(models.Model):
      names = models.CharField(max_length=255)
      email = models.EmailField(unique=True)
      phone = models.CharField(max_length=50)
      create_at = models.DateField(auto_now_add=True)

class Business(models.Model):
      business_type = models.CharField(max_length=255)
      tin = models.CharField(max_length=100)
      taxpayer_id = models.ForeignKey(Taxpayer, on_delete=models.CASCADE)

class Address(models.Model):
      city = models.CharField(max_length=100)
      ward = models.CharField(max_length=100)
      street = models.CharField(max_length=100)
      taxpayer_id = models.ForeignKey(Taxpayer,on_delete=models.CASCADE)

class Receipt(models.Model):
      receipt_no = models.CharField(max_length=255)
      number_of_items = models.CharField(max_length=20)
      item_name = models.CharField(max_length=40)
      cash_amount = models.DecimalField(decimal_places=2,max_digits=9999999999)
      total_inclusive_tax = models.DecimalField(decimal_places=2,max_digits=9999999999)
      total_exclusive_tax = models.DecimalField(decimal_places=2,max_digits=9999999999)
      created_at = models.DateField(auto_now_add=True)
      taxpayer_id = models.ForeignKey(Taxpayer,on_delete=models.CASCADE)