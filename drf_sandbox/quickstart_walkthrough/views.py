from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Cat

from .serializers import CatSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListCreateCatAPIView(ListCreateAPIView):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

class RetrieveUpdateDestroyCatAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()