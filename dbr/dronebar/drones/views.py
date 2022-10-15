from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import DroneModelForm, DroneTypeModelForm
from .models import Drone, DroneType
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import json
# from urllib.request import urlopen

# Create your views here.

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneListView(ListView):
    model = Drone

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneDetailView(DetailView):
    template_name = 'drones/drone_detail.html'
    model=Drone
    context_object_name = 'drone'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Drone,id=id_)

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneUpdateView(UpdateView):
    template_name = 'drones/drone_update.html'
    form_class = DroneModelForm
    model=Drone
    context_object_name = 'drone'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Drone,id=id_)



    # def get_success_url(self):
        # return reverse('shops:shop_list')
        # return reverse("shops:shop_detail" ,kwargs={"id":self.id})

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneDeleteView(DeleteView):
    template_name = 'drones/drone_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Drone,id=id_)

    def get_success_url(self):
        return reverse('drones:drone_list')

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneCreateView(CreateView):
    model = Drone
    template_name = 'drones/drone_create.html'
    form_class = DroneModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneTypeListView(ListView):
    model = DroneType

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneTypeDetailView(DetailView):
    template_name = 'drones/dronetype_detail.html'
    model=DroneType
    context_object_name = 'drone'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DroneType,id=id_)

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneTypeUpdateView(UpdateView):
    template_name = 'drones/drone_type_update.html'
    form_class = DroneTypeModelForm
    model=DroneType
    context_object_name = 'drone'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DroneType,id=id_)



    # def get_success_url(self):
        # return reverse('shops:shop_list')
        # return reverse("shops:shop_detail" ,kwargs={"id":self.id})

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneTypeDeleteView(DeleteView):
    template_name = 'drones/drone_type_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DroneType,id=id_)

    def get_success_url(self):
        return reverse('drones:drone_type_list')

# @login_required(login_url='login')
@method_decorator(login_required, name='dispatch')
class DroneTypeCreateView(CreateView):
    model = DroneType
    template_name = 'drones/dronetype_create.html'
    form_class = DroneTypeModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
