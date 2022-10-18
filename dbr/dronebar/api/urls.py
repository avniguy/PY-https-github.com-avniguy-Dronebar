from django.contrib import admin
from django.urls import path,include
from .views import (GetServiceSitesLocationsApiView, GetShopMenuApiView, CreateOrderApiView,
                    GetAnnouncementApiView, GetOrderStatusApiView, ScanAndCloseOrderApiView,
                    GetShopByServiceSiteApiView, CreateUserApiView, LoginUserApiView)

app_name='api'

urlpatterns = [
    path('api/user_create_api',CreateUserApiView,name='user_create_api'),
    path('api/user_login_api/<str:username>/<str:password>',LoginUserApiView,name='user_login_api'),
    path('api/shop_by_service_site/<str:pk>',GetShopByServiceSiteApiView,name='shop_by_service_site'),
    path('api/location_get_api/<str:lat2>/<str:lon2>',GetServiceSitesLocationsApiView,name='location_get_api'),
    path('api/menu_get_api/<str:pk>',GetShopMenuApiView,name='menu_get_api'),
    path('api/order_create_api',CreateOrderApiView,name='order_create_api'),
    path('api/announcement_get_api/<str:pk>',GetAnnouncementApiView,name='announcement_get_api'),
    path('api/order_ststus_get_api/<str:pk>',GetOrderStatusApiView,name='order_ststus_get_api'),
    path('api/scan_and_close_order_api/<str:pk>/<str:pk2>',ScanAndCloseOrderApiView,name='scan_and_close_order_api'),

]
