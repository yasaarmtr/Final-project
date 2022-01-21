from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("hello world")

def home(request):
    return render(request, 'web/template/home.html')

def product(request):
    return render(request, "web/template/product.html")

def gallery(request):
    return render(request, "web/template/gallery.html")

def signin(request):
    return render(request, "web/template/signin.html")

def cart(request):
    return render(request, "web/template/cart.html")
