from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from app_1.models import *
from . import *
import bcrypt

def logged_in_user(request):
    return User.objects.get(id=request.session['user_id'])

def login_register(request):
    context = {}
    return render(request, 'user_app/login_register.html', context)

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user/login_register')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
            )
    request.session['user_id'] = user.id
    return redirect('/')

def my_account(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register to view this page.')
        return redirect('/user/login_register') 
    loggedUser = User.objects.get(id=request.session['user_id'])
    orders = loggedUser.orders.all()
    context = {
        'user': loggedUser,
        'orders': orders
    }
    return render(request, 'user_app/my_account.html', context)

def process_edit_account(request):
    errors = User.objects.update_validator(request.POST)
    user = logged_in_user(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user/my_account')
    else:
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/my_account')
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/user/my_account')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user/login_register')
    else:
        user = User.objects.filter(email = request.POST['email'])
        request.session['user_id'] = user[0].id
        return redirect('/')
def logout(request):
    request.session.flush()
    return redirect('/')