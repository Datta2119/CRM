from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    contxt = {'orders': orders, 'customers': customers,}

    return render(request, 'accounts/dashboard.html', contxt)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customers(request):
    return render (request, 'accounts/customers.html')