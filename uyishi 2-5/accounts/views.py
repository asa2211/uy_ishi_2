from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser

class CreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer