from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

def RegisterView(request): # create new account
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account created for user: ' + user)
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

        if user is not None: # username and password are valid
            login(request , user)
            return redirect('index')
        else:     # username and password are NOT valid
            messages.info(request,"username or password is not correct")
            return render(request,'accounts/login.html',context)

    return render(request,'accounts/login.html',context)

def LogoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def ProfileView(request):
    context = {}
    user = request.user

    # try:
    if user is not None:
        context = {"user":user}
    else:
        messages.info(request,"username or password is not correct")
        return render(request,'accounts/login.html',context)

    if request.method == 'POST': 
        user.username = request.POST.get('username','')
        user.email = request.POST.get('email','')
        user.save()
        context["context_messages"] = "Your profile is updated"
    # except BaseException as e:
    #     context["error"]=str(e)
    #     return render(request,'error.html',context)

    return render(request,'accounts/profile.html',context)
