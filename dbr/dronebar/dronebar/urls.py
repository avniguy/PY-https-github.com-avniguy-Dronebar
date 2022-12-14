"""dronebar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from shops import urls
from drones import urls
from orders import urls
from accounts import urls
from api import urls
from accounts.views import LoginView


urlpatterns = [
    path("accounts/login", LoginView, name="login"),
    path("admin/", admin.site.urls),
    path("index/", views.index,name="index"),
    path("error/", views.error,name="error"),
    path("", views.index,name="homepage"),
    path("accounts/",include('accounts.urls')),
    path("shops/",include('shops.urls')),
    path("drones/",include('drones.urls')),
    path("orders/",include('orders.urls')),
    path("api/",include('api.urls')),
]
