from typing import Any
from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.
class User_Info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_number=models.CharField(max_length=50)
    agree=models.BooleanField(default=False)
    product_favorites=models.ManyToManyField(Product)

    # def __init__(self, *args: Any, **kwargs: Any) -> None:

    #     # self.user=kwargs["user"] 
    #     self.address=kwargs["address"] 
    #     self.address2=kwargs["address2"] 
    #     self.city=kwargs["city"] 
    #     self.state=kwargs["state"] 
    #     self.zip_number=kwargs["zip"] 
    #     self.agree= kwargs["agree"]


    def add_info(self,**kwargs):
        self.user=kwargs["user"] 
        self.address=kwargs["address"] 
        self.address2=kwargs["address2"] 
        self.city=kwargs["city"] 
        self.state=kwargs["state"] 
        self.zip_number=kwargs["zip"] 
        self.agree= kwargs["agree"]
   

    def __str__ (self):
        return self.user.username
