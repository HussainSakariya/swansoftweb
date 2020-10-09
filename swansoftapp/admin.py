from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)




