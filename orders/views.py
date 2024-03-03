from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product
from . models import Orders,OrderDetails,Payment
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
    total=0
    if  Orders.objects.all().filter(user=request.user,is_finished=False):
        order=Orders.objects.get(user=request.user,is_finished=False)
        order_detail=OrderDetails.objects.all().filter(order=order)
        temp=0
        for i in order_detail:
            total+=i.price*i.quantity
            temp=total-temp
            i.total=temp
          
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




def payment(request):
    data=None
    if request.method=="POST" :#and "btnpayment" in request.POST:
        #  if "ship_address" in request.POST and "ship_phone" in request.POST and "card_number" in request.POST and "expire" in request.POST and "csv" in request.POST :
            ship_address=request.POST["ship_address"]
            ship_phone=request.POST["ship_phone"]
            card_number=request.POST["card_number"]
            expire=request.POST["expire"]
            security_code=request.POST["csv"]
            if  Orders.objects.all().filter(user=request.user,is_finished=False):
                order=Orders.objects.get(user=request.user,is_finished=False)
                print("a1")
                payment=Payment(order=order,shipment_address=ship_address,shipment_phone=ship_phone,card_number=card_number,expire=expire,security_code=security_code)
                payment.save()
                print("a2")
                order.is_finished=True
                order.save()
                messages.success(request,"your order is finished")
                return redirect("my_order")

    else:
        if  Orders.objects.all().filter(user=request.user,is_finished=False):
            order=Orders.objects.get(user=request.user,is_finished=False)
            order_detail=OrderDetails.objects.all().filter(order=order)
            total=0
            for i in order_detail:
                total+=i.price*i.quantity
            data={"order":order,
                "order_detail":order_detail,
                "total":total}

    return render(request,"orders/payment.html",data)




def show_orders(request):
        data=None
        # order=None
        # order_detail=None
    #  if  Orders.objects.all().filter(user=request.user,is_finished=False):
        orders=Orders.objects.all().filter(user=request.user)
        if  orders:
           for x in orders:
                order=Orders.objects.get(id=x.id)
                order_detail=OrderDetails.objects.all().filter(order=order)
                total=0
                for i in order_detail:
                    total+=i.price*i.quantity
                x.total=total
                x.items_count =order_detail.count
              
        data={"order":orders}
        return render(request,"orders/show_order.html",data)