from django.db import models
import os
from django.db.models.signals import pre_save, post_save
import random
# Create your models here.
from products.utils import unique_slug_generator
from django.db.models import Q
# Create your models here.
from  products.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title


