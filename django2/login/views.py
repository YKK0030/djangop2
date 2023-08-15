from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"Templates/login/index.html")

def singup(request):

    return render(request,"Templates/login/singup.html")

def singin(request):
    return render(request,"Templates/login/singin.html")

def singout(request):
    return HttpResponse("ok")