# apis/views.py

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse("Hello, world!")