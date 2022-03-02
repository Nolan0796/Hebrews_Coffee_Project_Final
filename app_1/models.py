from email.mime import image
from django.db import models
from django.forms import CharField
from user_app.models import User


class OrderManager(models.Manager):
    def order_validator(self, postData):
        errors = {}
        if int(postData['quantity']) < 1:
            errors['quantity'] = "Your order must contain at least 1 drink."
        return errors
    

class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, null=True)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    small = models.DecimalField(max_digits=6, decimal_places=2)
    medium = models.DecimalField(max_digits=6, decimal_places=2)
    large = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, related_name="orders", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()
