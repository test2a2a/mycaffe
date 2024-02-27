from django.shortcuts import render,redirect

# Create your views here.
def add_to_card(request):
    return redirect("products")