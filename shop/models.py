from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.TextField()


    def __str__(self):
        return self.name

class Additional(models.Model):
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    additionals = models.ManyToManyField(Additional)
    preparation_time = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.product.name} - rasm"



class Comment(models.Model):
    text = models.CharField(max_length=500)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxLengthValidator(5)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text}"