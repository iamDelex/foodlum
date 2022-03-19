from distutils.command.upload import upload
from email.policy import default

from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

class Variety(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to='variety', default='variety.jpg', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
SPICEY = [
    ('Not', 'Not'),
    ('Mild', 'Mild'),
    ('Medium', 'Medium'),
    ('Hot', 'Hot'), 
    ('ExtraHot', 'ExtraHot')
]

class Meal(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    meal = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=False)
    menu = models.TextField()
    image = models.ImageField(upload_to= 'meal', default= 'meal.jpg', blank=True, null=True)
    spicy = models.CharField(max_length=100, choices=SPICEY, default='medium')
    time = models.CharField(max_length=50)
    discount = models.CharField(max_length=50, blank=True, null=True)
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=20)
    price = models.CharField(max_length=50)
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    display = models.BooleanField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal


class Meta:
    db_table = 'meal'
    managed = True
    verbose_name = 'Meal'
    verbose_name_plural = 'Meals'
    

STATUS = [
    ('New', 'New'),
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Closed', 'Closed'),
]

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='New')
    closed = models.DateTimeField(blank=True, null=True)  
    remark = models.TextField(blank=True, null=True)  
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
     
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile', default='male.jpg', blank=True, null=True)
    cart_code = models.AutoField(primary_key=True, serialize=True)
    
    
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'Profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
        
