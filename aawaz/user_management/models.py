from unicodedata import name
import uuid
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_img = models.ImageField(upload_to ='uploads/')
    mobile_number = models.CharField(max_length=15)