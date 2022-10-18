from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,"index.html")

@login_required(login_url='login')
def error(request):
    return render(request,"error.html")
