from django.shortcuts import render,get_object_or_404
from .models import Product
from accounts.models import User_Info
from django.contrib.auth.decorators import login_required 

# Create your views here.
def products(request):
    if "product_name" in request.GET and request.GET["product_name"]!= "":
        product_name=request.GET["product_name"]
        
        # request.GET["checkbox"]

        if "checkbox" in request.GET :# 
              if request.GET["checkbox"]=="on":
                  data=Product.objects.filter(name__contains=product_name)
        else:
                  data=Product.objects.filter(name__icontains=product_name)


        if "product_description" in request.GET:
            product_description=request.GET["product_description"]
            data=data.filter(description__icontains=product_description)
    else: 
       data=Product.objects.all()   
    
    if "product_from" in request.GET and  "product_to" in request.GET and request.GET["product_from"]!="":
        product_from=int(request.GET["product_from"])
        product_to=int(request.GET["product_to"])
        if product_from>=0 and product_to >=0 and  product_to>product_from:
           data= data.filter(price__gte=product_from ,price__lte=product_to)  #Greater than or equal

    
    return render(request,'products/products.html' ,context={"products":data})

@login_required
def product(request,id):
    
    favorite=1 if User_Info.objects.filter(user=request.user,product_favorites=id).exists() else 0
    # context={"item":Product.objects.get(id=id),"favorite":favorite}

    context={"item":get_object_or_404(Product,id=id),"favorite":favorite}
    
    return render(request,'products/product.html', context)


# http://127.0.0.1:8000/products/?product_name=&product_description=&product_from=5&product_to=25&checkbox=on
def search(request):
    return render(request,'products/search.html' )