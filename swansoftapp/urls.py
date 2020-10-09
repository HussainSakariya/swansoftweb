from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('prod_detail/<int:id>/',prod_detail,name='prod_detail'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('add_to_cart/',add_to_cart,name='add_to_cart'),
    path('ordrer/',order,name='order'),    
]