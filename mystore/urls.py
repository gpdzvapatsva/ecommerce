from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='index'),
    path('products/', views.products, name='products'),
path('cart/', views.cart, name='cart'),
path('contact/', views.contact, name='contact'),
]