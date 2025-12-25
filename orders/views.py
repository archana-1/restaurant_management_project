from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def create_order(request, pk=None):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        order = serializer.save()
        response_data = {
            "order_id":order.id,
            "status": "success",
            "customer": {
                "name": order.customer.name,
                "phone":order.customer.phone
            },
            "price": order.total_price
        }
        return Response(response_data)
    return Response(serializer.errors)