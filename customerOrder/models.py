from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    phone = PhoneNumberField(region="KE", null=False, blank=False, unique=True)
    def __str__(self):
        return f"{self.name} - {self.code}"

    

class Order(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.quantity}"