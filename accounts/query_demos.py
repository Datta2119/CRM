# Django DB Query Cheat Sheet.

from .models import *
# 01 | Return all customers from "Customer" Table

customers = Customer.objects.all()

# 02 | Return first customer in the table
first_customer = Customer.objects.first()

# 03 | Return last customer in the table
last_customer = Customer.objects.last()

# 04 | Return single customer by customer name from the table
customer_by_name = Customer.objects.get(name='Bishway Datta')

# 05 | Return single customer customer by customer id from the table
customer_by_id = Customer.objects.get(id=1)

# 06 | Return all orders related to customer (first customer variable is set above)
first_customer_orders = first_customer.order_set.all()

# 07 | Return orders by customers name (Query from parent model value)
orders = Order.objects.first()
parent_name = orders.customer.name

# 08 | Return products from products with the value of "Out Door" in category attribute
products = Product.objects.filter(category='Outdoor')

# 09| Order/Sort objects by id
least_to_greatest = Product.objects.all().order_by('id')
greatest_to_least = Product.objects.all().order_by('-id')

# 10 | Return all products with tag of "Sports" (Query Many to Many fields)
products_filtered = Product.objects.filter(tags_name='Sports')

# 11 | Bonus Question:

'''
Q: If the customer has more than 1 ball, how would it refelect in database?

A: Because there are many different products and this value changes constantly you would most likely
not want to store the value in the database but rather just make this a function we can run each time we load the customer profile

'''

# Return the total count for each product ordered
ballOrders = firstCustomer.order_set.filter(product__name='Ball').count()

# Returns total count for each product ordered:
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}

# Example Models:
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()

# Return all chil objects related to parents
parent.childmodel_set.all()