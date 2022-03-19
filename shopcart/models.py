from distutils.command.upload import upload
from email.policy import default

from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from foodie.models import Meal
# Create your models here.



class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    how_spicey = models.CharField(max_length=100)
    order_no = models.CharField(max_length=50)
    item_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
class Meta:
        db_table = 'Shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'
    
    
    
    
class Paidorder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=36)
    paid_item = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    
class Meta:
    db_table = 'Paidorder'
    managed = True
    verbose_name = 'paidorder'
    verbose_name_plural = 'paidorders'
    
    
    
STATUS = [
    ('new','new'),
    ('pending','pending'),
    ('processing','processing'),
    ('shipping','shipping'),
    ('delivered','delivered'),
]


class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True, null=True)
    shipping_no = models.CharField(max_length=50)
    paid_cart = models.BooleanField(default=False)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS, default='new', blank=True, null=True)
    state = models.CharField(max_length=50)
    admin_remark = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    
class Meta:
    db_table = 'shipping'
    managed = True
    verbose_name = 'shipping'
    verbose_name_plural = 'shippings'