from django.urls import path
from .views import MenuCategoryListAPIView

urlpatterns = [
    path("", MenuCategoryListAPIView.as_view(),name='MenuCategoryList' )
]