#Products and Search App
#Q
#Custom Search Query active and feature product query
#models.Manager for products



#products > models.py


#Defined query model related to product like active and featured products

from django.db import models
import os
from django.db.models.signals import pre_save, post_save
import random
# Create your models here.
from .utils import unique_slug_generator
from django.db.models import Q



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        #you can update icontains specs as you wish title__slug__icontains etc.
        lookups = (Q(title__icontains=query) |
                   Q(descriptios__icontains=query) |
                   Q(tag__title__icontains=query))

        return self.filter(lookups).distinct()
        
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):

        return self.get_queryset().active().search(query)
        
class Product(models.Model):
    title = models.CharField(max_length=250)
    slug =  models.SlugField(blank=True, unique=True)
    descriptios = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    object = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title
        
        
        
        
        
        
        
        
