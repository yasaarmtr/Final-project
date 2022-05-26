from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, '../templates/home.html')

def about(request):
    return render(request, '../templates/about.html')

def gallery(request):
    return render(request, '../templates/gallery.html')

def product(request):
    return render(request, '../templates/product.html')

def cart(request):
    return render(request, '../templates/cart.html')

def signin(request):
    return render(request, '../templates/signin.html')

def store(request):
    return render(request, '../templates/store.html')