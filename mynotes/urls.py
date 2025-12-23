from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import NoteViewSet ,login
from mynotes import views

router = DefaultRouter()
router.register(r'user', views.NoteViewSet, basename='notes')



urlpatterns =[
    path('', views.login,name = 'login' ),
]
urlpatterns += router.urls