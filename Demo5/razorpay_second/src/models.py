from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.CharField(max_length = 100)
    order_id = models.CharField(max_length=100,blank=True)  
    razorpay_payment_id = models.CharField(max_length = 100,blank=True)
    email = models.EmailField(max_length = 100)
    paid = models.BooleanField(default = False)