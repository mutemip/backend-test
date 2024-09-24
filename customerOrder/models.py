from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import africastalking
import logging
from django.conf import settings

sms = africastalking.SMS

class Customer(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    # phone = PhoneNumberField(region="KE", null=False, blank=False, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.name} - {self.code}"

    

class Order(models.Model):
    ITEMS = [
        ('Managu', 'Managu'),
        ('Terere', 'Terere'),
        ('Onion', 'Onion'),
    ]

    name = models.CharField(max_length=20, choices=ITEMS, default='Managu')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.quantity}"
    
    def __str__(self):
        return f"Order {self.id}"
    
    def get_total(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        self.send_sms()

    def send_sms(self):
        username = settings.S_AFRIKASTALKING_USERNAME
        print("USERNAME IS", username)
        api_key = settings.S_AFRIKASTALKING_API_KEY

        # Initialize the SDK
        africastalking.initialize(username, api_key)
        africastalking_sms = africastalking.SMS

        phone_no = "+254"+str(self.customer.phone)
        recipient = [phone_no]

        message = f"Thank you for your order! Item Name: {self.name} Item Price: {self.price} Quanity: {self.quantity} Total: {self.get_total()} Order ID: {self.id}"
        sender = settings.S_AFRIKASTALKING_APP_ID
        
        try:
            response = africastalking_sms.send(message, recipient, sender)
            print(response)
        except Exception as e:
            print(f"SMS sending failed: {str(e)}")

