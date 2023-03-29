from django.db import models
from django.contrib.auth.models import User

from shop.models import *


# Create your models here.
class CartData(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prod=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(CartData,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prod.name
    
    def total(self):
        return self.prod.price*self.quan