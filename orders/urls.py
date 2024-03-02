from django.urls import path
from . import views
urlpatterns = [
    path('add_to_cart', views.add_to_cart,name="add_to_cart"),
    path('my_cart', views.my_cart,name="my_cart"),
    path('delete_item/<int:id>', views.delete_item,name="delete_item"),
    path('sub_quantity/<int:id>', views.sub_quantity,name="sub_quantity"),
     path('add_quantity/<int:id>', views.add_quantity,name="add_quantity"),




]
