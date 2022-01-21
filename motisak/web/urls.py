from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('product', views.product, name='product'),
    path('gallery', views.gallery, name='gallery'),
    path('signin', views.signin, name='signin'),
    path('cart', views.cart, name='cart'),

]

#path(route, view, optional name)
# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route
