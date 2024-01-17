from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    data=Product.objects.all()
    return render(request,'products/products.html' ,context={"products":data})

def product(request):
    return render(request,'products/product.html' )



def search(request):
    return render(request,'products/search.html' )