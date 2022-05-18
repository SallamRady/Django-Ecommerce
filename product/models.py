from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='photoes/%y/%m/%d/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='product_user',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Review(models.Model):
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=3,decimal_places=2)
    product = models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.CASCADE)
    def __str__(self):
        return self.name


