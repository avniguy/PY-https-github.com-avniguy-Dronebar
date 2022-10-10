from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
# from django.contrib.auth.decorators import login_required

# @login_required('login')
def index(request):
    user = request.user
    context = {'user':user}
    return render(request,'index.html',context)
