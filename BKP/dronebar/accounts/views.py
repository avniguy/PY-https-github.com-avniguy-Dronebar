from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

def RegisterView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account created for user' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)

def LoginView(request):
    # form = CreateUserForm()
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            messages.info(request,"username or password is not correct")
            return render(request,'accounts/login.html',context)

    return render(request,'accounts/login.html',context)

def LogoutView(request):
    logout(request)
    return redirect('login')

# @method_decorator(login_required, name='dispatch')
@login_required(login_url='login')
def ProfileView(request):
    context = {}
    user = request.user

    if user is not None:
        context = {"user":user}
    else:
        messages.info(request,"username or password is not correct")
        return render(request,'accounts/login.html',context)

    return render(request,'accounts/profile.html',context)
