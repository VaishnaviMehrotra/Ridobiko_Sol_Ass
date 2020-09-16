from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db import models


# Create your models here.



class Index(models.Model):
    BrandName = models.CharField(max_length=100)
    BikeName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img1 = models.ImageField(upload_to='pics')
    store = models.TextField(max_length=300)
    price = models.IntegerField()

    #added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BrandName






