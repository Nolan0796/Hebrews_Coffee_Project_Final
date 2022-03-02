from django.urls import path, include
from . import views

urlpatterns = [
    path('login_register', views.login_register),
    path('register', views.register),
    path('my_account', views.my_account),
    path('process_edit_account', views.process_edit_account),
    path('login', views.login),
    path('logout', views.logout),
]
