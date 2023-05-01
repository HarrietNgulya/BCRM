from django.db import models
from django.contrib.auth.models import User

#create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,  null=True, blank=True, on_delete=models.SET_DEFAULT, default=None)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile photo1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name or ''

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name or ''

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'OutDoor'),
         ('Electronics| Smartphone ', 'Electronics | Smartphone'),
         ('Electronics| Laptop', 'Electronics | Laptop'),
         ('Electronics| Tablet', 'Electronics | Tablet'),
         ('Electronics| TVs', 'Electronics | TVs'),
         ('Electronics| Playstation', 'Electronics |  Playstation'),
         ('Apparel | Mens clothing', 'Apparel | Mens clothing'),
         ('Apparel | Womens clothing', 'Apparel | Womens clothing'),
         ('Apparel | Children clothing', 'Apparel | Children clothing'),
         ('Apparel | Shoes', 'Apparel | Shoes'),
         ('Apparel | Accessories', 'Apparel | Accessories'),



         
         
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name or ''


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_DEFAULT, default=None)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_DEFAULT, default=None)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name



    
    
 
   
        
    