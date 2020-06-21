from rest_framework.serializers import HyperlinkedModelSerializer
# from django.contrib.auth.models import User
from shoedata.models import Manufacturer, ShoeColor, ShoeType, Shoe, User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('id,', 'website')


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color_name')


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id',
                  'size',
                  'brand_name',
                  'manufacturer',
                  'color',
                  'material',
                  'shoe_type',
                  'fasten_type'
                  )

