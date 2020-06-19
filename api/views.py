from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import (ManufacturerSerializer, ShoeColorSerializer,
                             ShoeTypeSerializer, ShoeSerializer, UserSerializer)

from shoedata.models import (Manufacturer, Shoe, ShoeColor, ShoeType, User)

# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    base_name = 'manufacturer'
    queryset = Manufacturer.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    base_name = 'shoe'
    queryset = Shoe.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()