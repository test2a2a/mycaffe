from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
# Create your views here.
def index(request):
    data=Product.objects.all()

    return render(request,'pages/index.html' ,context={"products":data})

def about(request):
    return render(request,'pages/about.html' )

def Coffee(request):
    return render(request,'pages/Coffee.html')