#coding:utf8
from rest_framework import serializers
from models import Item,User,City

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','items',)

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id','item_name','user','city','is_use',)

class CitySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,read_only=True)
    class Meta:
        model = City
        fields = ('id','cityname','items',)


