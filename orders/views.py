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


        print(request)
        if not Product.objects.all().filter(id=pro_id).exists():
            return   redirect("products")
        product=Product.objects.get(id=pro_id)

        if order:
            messages.success(request,"was added to card for old order")
            old_order=Orders.objects.get(user=request.user,is_finished=False)
            order_details=OrderDetails.objects.create(product=product,order=old_order,price=product.price,quantity=pro_quantity)

        else:
            messages.success(request," was added to card for new order")
            new_order=Orders(user=request.user,orders_date=timezone.now(),is_finished=False)
            new_order.save()

            order_details=OrderDetails.objects.create(product=product,order=new_order,price=product.price,quantity=pro_quantity)

        return redirect("/products/"+request.GET["pro_id"])
    else:
        return redirect("products")
    
@login_required
def my_cart(request):
    if  Orders.objects.all().filter(user=request.user,is_finished=False):
        order=Orders.objects.get(user=request.user,is_finished=False)
        order_detail=OrderDetails.objects.all().filter(order=order)
        total=0
        for i in order_detail:
            total+=order_detail.price*order_detail.quantity
    data={"order":order,
          "order_detail":order_detail,
          "total":total}
    return render(request,"orders/cart.html",data)