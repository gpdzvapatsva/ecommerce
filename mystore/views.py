from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return  render (request, 'contact.html', context)
def products(request):
    context={}
    return  render (request, 'products.html')
def cart(request):
    context={}
    return  render (request, 'cart.html', context)
def contact(request):
    context={}
    return  render (request, 'contact.html', context)