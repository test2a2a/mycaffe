from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import User_Info,Product
from django.contrib.auth.decorators import login_required 
# Create your views here.

def signin(request):
    if request.method =="POST":
        username =request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user:
            if "rememberme"  not in request.POST:
                # request.session.set_expiry(0)
                print("xxxx")
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


@login_required
def profile(request):
     user_=User.objects.get(id=request.user.id)
     if request.method =="POST":
        
       
        user_.first_name=request.POST["first_name"]
        user_.last_name=request.POST["last_name"]
        if(not request.POST["password"].startswith("pbkdf2_sha256$")):
              user_.set_password(request.POST["password"]) 
              login(request,user_)

        user_.save()

        try:
            user_info=User_Info.objects.get(user=request.user)

            user_info.address=request.POST["address_1"]
            user_info.address2=request.POST["address_2"]
            user_info.city=request.POST["city"]
            user_info.state=request.POST["state"]
            user_info.zip_number=request.POST["zip"]
            user_info.save()
            messages.success(request," data is saved")
            return redirect("profile")
            

        except :

           

            data={ "user":user_,
            "address":request.POST["address_1"],
            "address2":request.POST["address_2"],
            "city":request.POST["city"],
            "state":request.POST["state"],
            "zip":request.POST["zip"],
            "agree": True,
            
            }
      

            user_info=User_Info()
            user_info.add_info(**data)
            user_info.save()
            messages.success(request,"success! data is saved")
            return redirect("profile")

            
        
    
     else:
         try:
            
           user_info=User_Info.objects.get(user=request.user)
         except :
           user_info=""
         data={"user_":user_,"user_info":user_info}
         return render(request,"accounts/profile.html",data)
     
     
#  User.password
# user_info.add

@login_required
def add_product_favorites(request ,id):
    pro_id=Product.objects.get(id=id)#id pk
    if User_Info.objects.filter(user=request.user,product_favorites=pro_id).exists():
        user=User_Info.objects.get(user=request.user)
        user.product_favorites.remove(pro_id)
        messages.success(request,"product has been deleted")

        # messages.error(request,"this product in the favorite list")
    else:
        user=User_Info.objects.get(user=request.user)
        user.product_favorites.add(pro_id)
        messages.success(request," product has been favorited")
    return redirect("/products/"+str(id))    

@login_required
def show_product_favorites(request ):
       user_=User_Info.objects.get(user=request.user) 
       
 

       return render(request,'products/products.html' ,context={"products":user_.product_favorites.all()})
   

