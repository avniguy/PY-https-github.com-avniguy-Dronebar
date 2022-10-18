from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def GetLocationApiView(request):
    pass

@api_view(['GET'])
def GetShopMenuApiView(request, pk): # pk of the shop (shop_id)
    pass

@api_view(['POST'])
def CreateOrderApiView(request):
    pass

@api_view(['GET'])
def GetAnnouncementApiView(request):
    pass

@api_view(['GET'])
def GetOrderStatusApiView(request, pk): # pk of the order (order_id)
    pass

@api_view(['GET', 'POST'])
def ScanAndCloseOrderApiView(request, pk): # pk of the order (order_id)
    pass
