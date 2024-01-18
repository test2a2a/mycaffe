from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.
def products(request):
    data=Product.objects.all()
    return render(request,'products/products.html' ,context={"products":data})

def product(request,id):
    context={"item":get_object_or_404(Product,id=id)}
    
    return render(request,'products/product.html', context)



def search(request):
    return render(request,'products/search.html' )