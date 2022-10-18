from rest_framework import serializers
from orders.models import Order, OrderRow
from drones.models import Drone, DroneType
from shops.models import Menu, MenuItem, Shop, ServiceSite
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'

class OrderRowSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderRow
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields = '__all__'

class ServiceSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceSite
        fields = '__all__'

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drone
        fields = '__all__'

class DroneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DroneType
        fields = '__all__'
