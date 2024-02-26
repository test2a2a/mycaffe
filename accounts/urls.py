from django.urls import path
from . import views
urlpatterns = [
 
    path('signin', views.signin,name="signin"),
    path('logout', views.logout_,name="logout"),
    path('signup', views.signup,name="signup"),
    path('profile', views.profile,name="profile"),
    path('add_product_favorites/<int:id>', views.add_product_favorites,name="add_product_favorites"),
    path('show_product_favorites', views.show_product_favorites,name="show_product_favorites"),


]
