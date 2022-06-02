from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, CreateAPIView
from .serializers import UserSerializer
from .models import User 
# Create your views here.
class UserApiListView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()