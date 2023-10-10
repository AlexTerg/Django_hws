from datetime import timedelta, datetime
import random
from django.http import HttpResponse
from django.shortcuts import render
from hws.models import User, Product, Order

# Create your views here.


def add_user(request):
    lst_user = []
    for i in range(10):
        user = User.objects.create(
            name=f'Name{i}', email=f'{i}xxx@xxx.com', phone=f'phone{i}', address=f'address{i}')
        lst_user.append(user)
    return HttpResponse(lst_user)


def add_product(request):
    lst_product = []
    for i in range(3):
        product = Product.objects.create(
            name=f'ProductName{i}', description=f'Description{i}', price=100 * random.random(), quantity=random.randint(1, 10))
        lst_product.append(product)
    return HttpResponse(lst_product)

def add_orders(request):
    lst_order = []
    # for i in range(5):
    #     user_id = random.randint(1, len(User.objects.all()))
    #     product_id = random.randint(1, len(Product.objects.all()))
    #     order = Order.objects.create(
    #         costumer=user_id, products=product_id
    #     )
    #     lst_order.append(order)\
    user = User.objects.get(pk=random.randint(1, len(User.objects.all())))
    total_price = 0
    order = Order(customer=user)
    for i in range(1, 5):
        product = Product.objects.filter(pk=random.randint(1, len(Product.objects.all()))).first()
        total_price += product.price
        order.total_price = total_price
        order.save()
        order.products.add(product)
        lst_order.append(order)
        
        
    return HttpResponse(lst_order)

def index(request):
    return render(request, 'base.html')

def get_user_orders(request, user_id, days_ago):
    products = []
    product_lst =[]
    date_now = datetime.now()
    date_before = date_now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered__range=(date_before, date_now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_lst:
                product_lst.append(product)

    return render(request, 'user_orders.html', {'user': user, 'product_lst': product_lst, 'day': days_ago})