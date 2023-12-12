from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="plane_images", default="/static/plane_images/Hobbit.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Kids', 'Kids'),
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Home appliances', 'Home Appliances'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other')


    def __str__(self):
        return self.name 
    
class Cart(models.Model):
    is_paid = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart ({self.cart.user.username})"