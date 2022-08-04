from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from admin_panel.drop_down_choices import Choices
from user_management.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Product(BaseModel):
    product_type = models.CharField(max_length=50, choices=Choices.product_type)
    package_type = models.CharField(max_length=50, choices=Choices.product_type)
    product_name = models.CharField(max_length=120)
    product_image = models.ImageField(upload_to = 'upload/products/')
    product_rate = models.FloatField(default=0.00)
    number_in_bundle = models.IntegerField(default=0)
    extra_product = models.IntegerField(default=0)

    @property
    def price(self):
        
        return self.product_rate * self.number_in_bundle
    def __str__(self):
        return self.product_name

class Coin(BaseModel):
    coin_name = models.CharField(max_length=120)
    coin_image = models.ImageField(upload_to = 'upload/products/coin')
    coin_rate = models.FloatField(default=0.00)
    def __str__(self):
        return self.coin_name

class Diamond(BaseModel):
    diamond_name = models.CharField(max_length=120)
    diamond_image = models.ImageField(upload_to = 'upload/products/diamond')
    diamond_rate = models.FloatField(default=0.00)
    def __str__(self):
        return self.diamond_name

class Gift(BaseModel):
    gift_name = models.CharField(max_length=120)
    gift_image = models.ImageField(upload_to = 'upload/products/gift')
    gift_rate = models.FloatField(default=0.00)
    def __str__(self):
        return self.gift_name


