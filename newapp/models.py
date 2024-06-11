from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=50,decimal_places=0)
    Payment_way = (
        ('Credit Card','Credit Card'),
        ('PayPal','PayPal'),
    )
    payment_method=models.CharField(max_length=50,default='Credit Card', choices=Payment_way)
    STATUS = (
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Failed','Failed'),
    )
    status = models.CharField(default='Pending',max_length=50, choices=STATUS)

class Poll(models.Model):
    question = models.CharField(max_length=255)
    pub_date=models.DateTimeField()

class Choice(models.Model):
    choice_text = models.CharField(max_length =255)
    votes = models.PositiveIntegerField(default=0)
    