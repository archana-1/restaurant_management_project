from django.shortcuts import render
from  rest_framework.generics import ListAPIView
from .serializers import MenuCategorySerializer
from .models import MenuCategory
# Create your views here.

class MenuCategoryListAPIView(ListAPIView):
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all()
    
