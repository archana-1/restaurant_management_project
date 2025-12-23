from django.urls import path
from .views import *

urlpatterns = [
    path('',restaurants, name= 'getrestaurants'),
    path('restaurant/<int:pk>',restaurants, name= 'getrestaurant'),
    path('register', register_restaurant, name= 'register'),
    path('update/<int:pk>', register_restaurant, name= 'update'),
    path('delete/<int:pk>', delete_restaurant, name= 'delete'),


    path('staff/login', StaffLoginAPIView.as_view(), name = "staff_login"),
   
   
   # pk is the id of the restaurant
    path('restaurant/<int:pk>/menuitems/', menuitems, name='getmenuitems'),
    # pk is the id of the menuitem
    path('menuitem/<int:pk>', menuitems, name='getmenuitem'),
    path('restaurant/<int:pk>/menuitem/create', create_menuitem, name="create_menuitem"),
    path('menuitem/update/<int:pk>', update_menuitem, name='updatemenuitem'),
    path('menuitem/delete/<int:pk>', delete_menuitem, name='deletemenuitem'),
    

    path('customers/', get_customers, name = 'get_customers'),
    path('customer/create', create_customer, name = 'create_customer')
    ]