from cgitb import small
from django.shortcuts import render, redirect
from user_app.models import User
from .models import *
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "app_1/index.html", context)
    else: 
        return render(request, "app_1/index.html")

def menu(request):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'drinks': Drink.objects.all()
        }
    else:
        context = {
            'drinks': Drink.objects.all()
        }
    return render(request, "app_1/menu.html", context)

def order(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register to place an order.')
        return redirect('/user/login_register')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'drinks': Drink.objects.all(),
        'quantity': [0,1,2,3,4,5]
    }
    return render(request, "app_1/order.html", context)

def process_order(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register to place an order.')
        return redirect('/user/login_register')
    errors = Order.objects.order_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/order')
    if request.POST['size'] == "small":
        smallDrink = Drink.objects.get(id=request.POST['drink'])
        total = int(request.POST['quantity']) * smallDrink.small
    elif request.POST['size'] == "medium":
        mediumDrink = Drink.objects.get(id=request.POST['drink'])
        total = int(request.POST['quantity']) * mediumDrink.medium
    else:
        largeDrink = Drink.objects.get(id=request.POST['drink'])
        total = int(request.POST['quantity']) * largeDrink.large

    newOrder = Order.objects.create(
        user = User.objects.get(id=request.session['user_id']),
        drink = Drink.objects.get(id=request.POST['drink']),
        total = total
    )
    return redirect('order-confirmation/' + str(newOrder.id))

def order_confirmation(request, order_id):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'order': Order.objects.get(id=order_id)
    }
    return render(request, "app_1/order_confirmation.html", context)

















    # if 'user_id' not in request.session:
    #     messages.error(request, 'Please log in or register to proceed.')
    #     return redirect('/')
    # user = User.objects.get(id=request.session['user_id'])
    # context = {
    #     'user': user
    # }
    # return render(request, 'user_app/success.html', context)
