from django.contrib import admin
from django.urls import path,include
from .views import RegisterView, LoginView, LogoutView, ProfileView

# from .views import (DroneListView, DroneCreateView, DroneDetailView, DroneDeleteView, DroneUpdateView,
# DroneTypeListView, DroneTypeCreateView, DroneTypeDetailView, DroneTypeUpdateView, DroneTypeDeleteView)
# #
app_name='accounts'

urlpatterns = [
    path('register/',RegisterView,name='register'),
    path('login/',LoginView,name='login'),
    path('profile/',ProfileView,name='profile'),
    path('logout/',LogoutView,name='logout'),

]
