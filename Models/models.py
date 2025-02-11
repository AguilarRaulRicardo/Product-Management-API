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
    stock = models.IntegerField()
    image = models.CharField(max_length=150, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    user_id= models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'user_id'], name='unique_review_per_product')
        ]
