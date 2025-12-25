from rest_framework import serializers
from .models import Restaurant, MenuItem, Customer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields= ['name', 'owner_name', 'address' ]

class StaffLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =serializers.CharField(write_only = True)    

# MenuItem serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

#CustomerSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
