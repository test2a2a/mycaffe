from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import User_Info
# Create your views here.

def signin(request):
    # if request.GET:
    messages.info(request,"info")
    messages.success(request,"success")
    messages.error(request,"error")

    return render(request,"accounts/signin.html")

def signup(request):                 #     first_name,last_name,address_1,address_2,city,state,zip,email,username ,password  ,agree  
    if request.method =="POST":
       
        email=request.POST["email"]
        username =request.POST["username"]
        password=request.POST["password"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        user=User.objects.create_user(username, email, password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        
        data={ "user":user,
               "address":request.POST["address_1"],
               "address2":request.POST["address_2"],
               "city":request.POST["city"],
               "state":request.POST["state"],
               "zip":request.POST["zip"],
               "agree": True if request.POST["agree"]=="on" else False,
              
              }
        
        # try:
        #     pass
        # except Exception as e:
        #    print(e) 


        user_info=User_Info()
        user_info.add_info(**data)
        user_info.save()
        return redirect('signin')
    else:    
       return render(request,"accounts/signup.html")



def profile(request):
    return render(request,"accounts/profile.html")