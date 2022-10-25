from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Favorite(models.Model):
    """
    A Favorite model so users can save products as their favorites
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

