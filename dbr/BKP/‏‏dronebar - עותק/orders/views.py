from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from .forms import OrderModelForm
from .models import Order
from .filters import OrderCreateFilter

import datetime

from .forms import ShopOptionForm
from shops.models import Menu, MenuItem, Shop, ServiceSite  # START THIS IS A TEST FOR CREATING A NEW ORDER JUST LIKE IN THE APP


# Create your views here.

# def OrderSearchView(request):
#     order = Order.objects.all()
#     my_filter = OrderFilter(request.GET, queryset=order)
#     order = my_filter.qs
#     context = {'my_filter':my_filter,'orders':order}
#     return render(request,'orders/order_search.html',context)

def OrderCreateView(request):
    form = ShopOptionForm(request.GET)
    context = {'form':form}
    menu = Menu.objects.all()

    if request.method =='GET':
        if form.is_valid():
            shop_id = form.cleaned_data.get('shop')
            shop_details = Shop.objects.get(id=shop_id)

            if shop_details.menu is None:
                context = {'form':form}
                context['error_msg'] = "This shop has no menu to choose from"
            else:
                context = {'form':form}
                context['error_msg'] = ""
                context['shop_id'] = shop_id
                menu_details = Menu.objects.get(id = shop_details.menu.id)
                items = menu_details.items.all()
                context['menu_items'] = items


    # return render(request,'orders/popeye.html',context)
    return render(request,'orders/order_create.html',context)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'

# class OrderDetailView(DetailView):
#     template_name = 'orders/order_detail.html'
#     model=Order
#     context_object_name = 'order'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Order,id=id_)
#
# class OrderUpdateView(UpdateView):
#     template_name = 'orders/order_update.html'
#     form_class = OrderModelForm
#     model=Order
#     context_object_name = 'order'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Order,id=id_)
#
#     def get_success_url(self):
#         id_ = self.kwargs.get("id")
#         return reverse("orders:order_detail",kwargs={"id":id_})
#
class OrderDeleteView(DeleteView):
    template_name = 'orders/order_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order,id=id_)

    def get_success_url(self):
        return reverse('orders:order_list')

# class OrderCreateView(CreateView):
#     # model = Order
#     template_name = 'orders/order_create.html'
#     # form_class = OrderModelForm
#     shop = Shop.objects.all()
#
#
#
#     def form_valid(self,form):
#         self.object = form.save()
#         print(form.cleaned_data)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('orders:order_list')
