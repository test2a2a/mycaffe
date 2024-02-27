from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone
# Create your models here.

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orders_date=models.DateTimeField(default =timezone.now)
    details=models.ManyToManyField(Product,through="OrderDetails")
    is_finished=models.BooleanField()
    # def __str__(self):
    #     return "u_"+self.user.username+"_o_"+str(self.id)
    


class OrderDetails(models.Model): 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    quantity=models.IntegerField()

    # def __str__(self):
    #     return "u_"+self.order.user.username+"_p_"+str(self.product.name)+"_o_"+str(self.id)
