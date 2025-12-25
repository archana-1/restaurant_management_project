from django.shortcuts import render, get_object_or_404, redirect
from .serializers import RestaurantSerializer,StaffLoginSerializer, MenuItemSerializer, CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, MenuItem, Customer
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from django.urls import reverse

# Create your views here.
@api_view(['GET'])
def menuitems(request, pk= None):
    restaurant = Restaurant.objects.get(pk = pk )
    menuitems = MenuItem.objects.filter(restaurant= restaurant)
    serializer = MenuItemSerializer(menuitems, many= True)
    return Response(serializer.data)
@api_view(['PUT'])
def update_menuitem(request, pk = None):
    menuitem = MenuItem.objects.get(pk = pk)
    serializer = MenuItemSerializer(menuitem, data= request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK)
    return Response(serializer.errors)

@api_view(['POST'])
def create_menuitem(request, pk=None):
    serializer = MenuItemSerializer(data= request.data)
    restaurant = Restaurant.objects.get(pk =pk)
    if serializer.is_valid():
        serializer.save(restaurant=restaurant)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_menuitem(request, pk = None):
    menuitem = MenuItem.objects.get(pk = pk)
    menuitem.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def restaurants(request, pk = None):
    if pk is not None:
        restaurant = get_object_or_404(Restaurant, pk = pk) 
        serializer = RestaurantSerializer(restaurant)
    elif pk is None:
        # list all restaurants
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
    
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_restaurant(request, pk = None):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)






@api_view(['POST', 'PUT'])
def register_restaurant(request, pk =None):
    
    if pk is not None:
        # updates the restaurant
        restaurant = get_object_or_404(Restaurant, pk = pk)
        serializer = RestaurantSerializer(restaurant, data = request.data, partial = True)
    elif pk is None:
        # register restaurant
        serializer = RestaurantSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.errors)


# CLASS FOR STAFF LOGIN API
class StaffLoginAPIView(APIView):
    

    def get(self, request):
        
        serializer = StaffLoginSerializer()
        return Response(serializer.data)
    
    def post(self, request):
        serializer  = StaffLoginSerializer(data = request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            User  = get_user_model()    
            myuser = User.objects.get(email = email)
            res_id  = myuser.restaurant.id # restaurant id
            if myuser.check_password(password) and myuser.is_staff:
                # return Response({"message": "Login Successfull", "staff_id": myuser.id}, status=status.HTTP_200_OK)
                url = reverse('getmenuitems', kwargs={'pk': res_id})
                return redirect (url)

            return Response({"error": "Invalid creds"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)  
    return Response(serializer.data)

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )