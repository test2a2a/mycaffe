from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import User_Info
# Create your views here.

def signin(request):
    if request.method =="POST":
        username =request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("profile")
        else:
            messages.error(request,"the username or password invalid")
    # messages.info(request,"info")
    # messages.success(request,"success")
    # messages.error(request,"error")

    return render(request,"accounts/signin.html")

def signup(request):                 #     first_name,last_name,address_1,address_2,city,state,zip,email,username ,password  ,agree  
    if request.method =="POST":
       
        email=request.POST["email"]
        username =request.POST["username"]
        password=request.POST["password"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        

        data_={ "email":email,
        "username":username,
        "password":password,
        "first_name":first_name,
        "last_name":last_name,
        "address":request.POST["address_1"],
        "address2":request.POST["address_2"],
        "city":request.POST["city"],
        "state":request.POST["state"],
        "zip":request.POST["zip"],
       
        
        }

        if (User.objects.filter(username=username).exists() ):
            messages.error(request,"THIS USERNAME IS TOKEN")
            return render(request,"accounts/signup.html",data_)
        elif (User.objects.filter(email=email).exists() ):
            messages.error(request,"THIS EMAIL IS TOKEN")
            # re
            return render(request,"accounts/signup.html",data_)
        else:

            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password)
            # user.first_name=first_name
            # user.last_name=last_name
            user.save()

            if "check" in request.POST:
                check= True 
            else:
                check= False 
        
            data={ "user":user,
                "address":request.POST["address_1"],
                "address2":request.POST["address_2"],
                "city":request.POST["city"],
                "state":request.POST["state"],
                "zip":request.POST["zip"],
                "agree": check,
                
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


def logout_(request):
    logout(request)
    return redirect('signin')
def profile(request):
    return render(request,"accounts/profile.html")