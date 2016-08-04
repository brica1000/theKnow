from django.db import models

from django.utils import timezone




class Orders(models.Model):
    customer = models.CharField(max_length=200)
    order_date = models.DateField(default=timezone.now)
    order_slot = models.CharField(max_length=200)
    order_details = models.TextField()
