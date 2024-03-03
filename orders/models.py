from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

from creditcards .models import CardNumberField,CardExpiryField,SecurityCodeField

# Create your models here.

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orders_date=models.DateTimeField(default =timezone.now)
    details=models.ManyToManyField(Product,through="OrderDetails")
    is_finished=models.BooleanField()
    total=0
    items_count=0
    # def __str__(self):
    #     return "u_"+self.user.username+"_o_"+str(self.id)
    


class OrderDetails(models.Model): 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    quantity=models.IntegerField()
    total=0

    class Meta:
        ordering=["id"]

    # def __str__(self):
    #     return "u_"+self.order.user.username+"_p_"+str(self.product.name)+"_o_"+str(self.id)


class Payment(models.Model):
  order=models.ForeignKey(Orders,on_delete=models.CASCADE)
  shipment_address=models.CharField(max_length=150)
  shipment_phone=models.CharField(max_length=50)
  card_number=CardNumberField()
  expire=CardExpiryField()
  security_code=SecurityCodeField()

