from django.contrib import admin
from django.urls import path,include
from .views import (GetLocationApiView, GetShopMenuApiView, CreateOrderApiView,
                    GetAnnouncementApiView, GetOrderStatusApiView, ScanAndCloseOrderApiView)

app_name='api'

urlpatterns = [
    path('api/location_get_api',GetLocationApiView,name='location_get_api'),
    path('api/menu_get_api/<str:pk>',GetShopMenuApiView,name='menu_get_api'),
    path('api/order_create_api',CreateOrderApiView,name='order_create_api'),
    path('api/announcement_get_api',GetAnnouncementApiView,name='announcement_get_api'),
    path('api/order_ststus_get_api/<str:pk>',GetOrderStatusApiView,name='order_ststus_get_api'),
    path('api/scan_and_close_order_api/<str:pk>',ScanAndCloseOrderApiView,name='scan_and_close_order_api'),

]
