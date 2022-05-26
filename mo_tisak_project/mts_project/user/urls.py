from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('signout/', views.signout, name='signout'),
    path('login/', views.login, name="login"),

]