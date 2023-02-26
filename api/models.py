from django.db import models

# Create your models here.

class Category(models.Model):
    item = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

class ProductApi(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    selling_price = models.PositiveIntegerField(default=0)
    market_price = models.PositiveIntegerField(default=0)


