from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('product', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('signin', views.signin, name='signin'),
    path('store', views.store, name='store'),


]
