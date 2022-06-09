from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_of_delivery = orders.filter(status='Out of Delivery').count()

    contxt = {
        'orders': orders, 
        'customers': customers, 
        'total_orders': total_orders, 
        'delivered': delivered, 
        'pending': pending,
        'out_of_delivery': out_of_delivery,
        }

    return render(request, 'accounts/dashboard.html', contxt)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customers(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    orders_count = orders.count()
    contxt = {
        'customers':customers,
        'orders': orders,
        'orders_count': orders_count
    }
    return render (request, 'accounts/customers.html', contxt)