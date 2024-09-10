from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

class Brand(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ManyToManyField(Category)
    brand = models.ManyToManyField(Brand)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    price = models.FloatField()
    Stock = models.IntegerField()
    #img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)