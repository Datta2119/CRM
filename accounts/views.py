from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from accounts import forms
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

def createOrder(request):
    form = OrderForm()

    if request.method == 'post' or 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form_contxt = {'form': form}
    
    return render (request, 'accounts/order_form.html', form_contxt)

def updateOrder(request, pk):
    orders = Order.objects.get(id=pk)
    form = OrderForm(instance=orders)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    update_context = {'form': form}

    return render (request, 'accounts/order_form.html', update_context)

def deleteOrder(request, pk):
    orders = Order.objects.get(id=pk)

    if request.method == 'POST':
        orders.delete()
        return redirect('/')

    delete_context = {'item': orders}
    return render(request, 'accounts/delete.html', delete_context)