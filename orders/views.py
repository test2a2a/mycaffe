from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product
from . models import Orders,OrderDetails
from django.utils import timezone
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required
def add_to_cart(request):

    if 'pro_id' in request.GET and 'pro_quantity' in request.GET and 'pro_price' in request.GET : #request.user.is_authenticated:
        pro_id=request.GET["pro_id"]
        pro_quantity=request.GET["pro_quantity"]
        pro_price=request.GET["pro_price"]
        order=Orders.objects.all().filter(user=request.user,is_finished=False)


        # print(request)
        if not Product.objects.all().filter(id=pro_id).exists():
            return   redirect("products")
        product=Product.objects.get(id=pro_id)

        if order:
            messages.success(request,"was added to card for old order")
            old_order=Orders.objects.get(user=request.user,is_finished=False)
            if OrderDetails.objects.all().filter(order=old_order,product=product).exists():
                  order_detail=OrderDetails.objects.get(order=old_order,product=product)
                  order_detail.quantity+=int(pro_quantity)
                  order_detail.save()
            else:     
               OrderDetails.objects.create(product=product,order=old_order,price=product.price,quantity=pro_quantity)

        else:
            messages.success(request," was added to card for new order")
            new_order=Orders(user=request.user,orders_date=timezone.now(),is_finished=False)
            new_order.save()

            OrderDetails.objects.create(product=product,order=new_order,price=product.price,quantity=pro_quantity)

        return redirect("/products/"+request.GET["pro_id"])
    else:
        return redirect("products")
    
@login_required
def my_cart(request):
    data=None
    if  Orders.objects.all().filter(user=request.user,is_finished=False):
        order=Orders.objects.get(user=request.user,is_finished=False)
        order_detail=OrderDetails.objects.all().filter(order=order)
        total=0
        for i in order_detail:
            total+=i.price*i.quantity
        data={"order":order,
            "order_detail":order_detail,
            "total":total}
        
    return render(request,"orders/cart.html",data)


def delete_item(request,id):
         order_detail=OrderDetails.objects.get(id=id)
         if request.user.id==order_detail.order.user.id:
              order_detail.delete()
         return redirect('my_cart')


def add_quantity(request,id):
      order_detail= OrderDetails.objects.get(id=id)
      order_detail.quantity+=1
      order_detail.save()
      return redirect('my_cart')

def sub_quantity(request,id):
      order_detail= OrderDetails.objects.get(id=id)
      if order_detail.quantity>1:
          order_detail.quantity-=1
          order_detail.save()
      return redirect('my_cart')