from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from .models import AppUser, Group
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse_lazy

# Create your views here.
def CreateUser(request):
    form = CreateUserForm()
    context = {'form':form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for user:'+ user)
            return redirect('login')
        else:
             print(form.errors)
             return render(request,'appusers/user_create.html',{'form':form})

    return render(request,'appusers/user_create.html',context)

#*************************************************************

def DeleteUser(request):
    return render(request,'appusers/user_delete.html')
#*************************************************************
# @login_required('login')
def UserDetail(UpdateView):
    return render(request,'appusers/user_detail.html')
#*************************************************************
# @login_required('login')
class UserList(ListView):
    model = AppUser
    # return render(request,'appusers/user_list.html')
#*************************************************************
def UserLogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password incorrect')
            return render(request,'appusers/user_login.html',context)

    return render(request,'appusers/user_login.html')
#*************************************************************
# @login_required('login')
def UserLogout(request):
    logout(request)
    return redirect('login')
