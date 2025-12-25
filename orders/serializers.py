from rest_framework import serializers
from account.models import Customer, MenuItem, Restaurant
from .models import Order
from account.serializers import CustomerSerializer, MenuItemSerializer
class OrderSerializer(serializers.Serializer):
    customer = serializers.DictField()
    items = serializers.ListField(
        child  = serializers.CharField()
    )
    res_id = serializers.IntegerField()

    def create(self, validated_data):
        total_price = 0  
        res_id = validated_data["res_id"]
        customer = validated_data.pop('customer')
        items= validated_data.pop('items') 
        # lower case
        for item in items:
            item  = item.lower()
        # get the restaurant
        restaurant = Restaurant.objects.get(id = res_id)
        # create customer
        customer, created = Customer.objects.get_or_create(
                name=customer['name'],
                phone = customer['phone']
               
            )

        # calculate total price
        menu_items  = MenuItem.objects.filter(name__in=items,restaurant= restaurant)
        for item in menu_items:
            if item.is_available and item.restaurant.id == res_id:
                total_price += item.price
        
        #create the order for that customer id
        order = Order.objects.create(customer=customer, total_price= total_price, restaurant =restaurant)
        return order