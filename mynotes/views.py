from django.shortcuts import render, redirect

from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


# get query_set
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner = user)

# CREATE 
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# update items  
    def update(self, request, pk=None):
        pass


@api_view(['POST'])
def login(request):
    username = request.data.get('username').strip()
    password = request.data.get('password').strip()

    

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/api/notes/user/')
        
