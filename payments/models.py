from django.db import models

# Create your models here.

class Payment(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id=models.CharField(max_length=255)
    status = models.CharField(max_length=255,default = 'pending')
    date_created = models.DateTimeField(auto_now_add=True)
    
    