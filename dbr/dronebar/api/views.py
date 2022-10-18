from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from orders.models import Order, OrderRow
from drones.models import Drone, DroneType
from shops.models import Menu, MenuItem, Shop, ServiceSite
from .serializers import ShopSerializer, OrderSerializer, MenuItemSerializer,ServiceSiteSerializer
import math

# Create your views here.

@api_view(['GET']) # WORKS OK
def GetShopByServiceSiteApiView(request, pk): # pk of the service_site (service_site_id)
    shop = Shop.objects.get(service_site_id=pk)
    serializer = ShopSerializer(shop,many=False)

    return Response(serializer.data)

@api_view(['GET']) # WORKS OK
# returns all service_sites within 800 meters or less away from you
def GetServiceSitesLocationsApiView(request,lat2,lon2):
    def round_down(num):
        return math.floor(num * 100) / 100

    lt=round_down(float(lat2))
    ln=round_down(float(lon2))
    sites = ServiceSite.objects.filter(lat__range=((lt),(lt+0.01)), long__range=((ln),(ln+0.01)))

    serializer = ServiceSiteSerializer(sites,many=True)

    return Response(serializer.data)

    # earthRadiusKm = 6371
    # dLat = degreesToRadians(lat2-lat)
    # dLon = degreesToRadians(lon2-lon)
    #
    # lat1 = degreesToRadians(lat)
    # lat2 = degreesToRadians(lat)
    #
    # a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat) * math.cos(lat2)
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    #
    # distanceInKM=earthRadiusKm * c
    # print(str(distanceInKM))
    # # return earthRadiusKm * c
    #
    # def degreesToRadians(degrees):
        # return degrees * math.pi / 180

@api_view(['GET']) # WORKS OK
def GetShopMenuApiView(request, pk): # pk of the shop (shop_id)
    menu_id = Shop.objects.get(id=pk).menu_id
    menu = Menu.objects.get(id=menu_id)
    items = menu.items
    serializer = MenuItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST']) # WORKS OK
def CreateOrderApiView(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response('OK')
    else:
        return Response('NOT-VALID')

    return Response('NO-DATA')

@api_view(['GET']) # WORKS OK
def GetOrderStatusApiView(request, pk): # pk of the order (order_id)
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order,many=False)
    return Response(serializer.data)

@api_view(['GET'])  # WORKS OK
# example for url QRCODE: http://127.0.0.1:8000/api/api/scan_and_close_order_api/139
# if my app current order is the same id then it will match
def ScanAndCloseOrderApiView(request, pk, pk2): # pk of the order (order_id), pk2=clientOrder pk
    if pk == pk2:
        order = Order.objects.get(id=pk)
        order.status = 'Delievered'

        serializer2 = OrderSerializer(order)
        serializer = OrderSerializer(instance=order,data=serializer2.data)

        if serializer.is_valid():
            serializer.save()
            return Response("ORDER_UPDATED")
        else:
            return Response("NOT_VALID")
    else:
        return Response("NOT_YOUR_ORDER")

    return Response('NO-DATA')

@api_view(['GET'])
def GetAnnouncementApiView(request, pk):
    pass
