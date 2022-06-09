from django.forms import ModelForm
from numpy import product
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'