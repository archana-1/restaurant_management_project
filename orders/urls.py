from django.urls import path
from .views import *

urlpatterns = [
   path('restaurant/<int:pk>/create_order', create_order, name= 'create_order')

]