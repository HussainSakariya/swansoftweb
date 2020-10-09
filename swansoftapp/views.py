from os import error

from django.http import JsonResponse
from swansoftapp.models import Products
from django.contrib.admin.decorators import register
from django.urls.base import reverse
from swansoftapp.forms import UserForm
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *
#Note:i know classbase views also but i used function baseviwes

@login_required(login_url='login/')
def index(request):
    prod=Products.objects.all()
    return render(request,'index.html',{'products':prod})

@login_required(login_url='login/')
def prod_detail(request,id):
    product=Products.objects.get(id=id)
    return render(request,'prod_detail.html',{'product':product})

def register(request):
    frm=UserForm(request.POST or None)
    if request.method=='POST':
        if frm.is_valid():
            frm.save()
            return redirect(reverse('login'))
    else:
        return render(request,'register.html',{'frm':frm})

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request, email=email,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect(reverse('index'))
        else:
            return render(request,'login.html',{'error_msg':"Please Enter Proper Email & Password"})
    else:
        return render(request,'login.html')

@login_required(login_url='login/')
def logout(request):
    auth_logout(request)    
    return redirect(reverse('index'))

@login_required(login_url='login/')
def add_to_cart(request):
    product=request.GET.get('prod_id')
    qty=request.GET.get('qty')
    print("producttt",product,qty)
    totprice=int(Products.objects.get(id=product).price) * int(qty)

    data={'msg':'pending'}
    if Cart.objects.filter(user=request.user).exists():
        if CartItem.objects.filter(cart__user=request.user,product=product).exists():
            c1=CartItem.objects.get(cart__user=request.user,product=product)
            c1.cart=Cart.objects.get(user=request.user)
            c1.product=Products.objects.get(id=product)
            c1.qty=qty
            c1.totprice=totprice
            c1.save()
            data = {'msg': "Cart Updated"}
        else:
            print("addtocart")
            c1=CartItem()
            c1.cart=Cart.objects.get(user=request.user)
            c1.product=Products.objects.get(id=product)
            c1.qty=qty
            c1.totprice=totprice
            c1.save()
            data = {'msg': "Add To Cart"}
    else:
        Cart.objects.create(user=request.user)
        c1=CartItem()
        c1.cart=Cart.objects.get(user=request.user.id)
        c1.product=Products.objects.get(id=product)
        c1.qty=qty
        c1.totprice=totprice
        c1.save()
        data = {'msg': "Cart Created"}

    prod=Products.objects.get(id=product)
    prod.qty=prod.qty-qty
    prod.save()
    return JsonResponse(data)     
    

@login_required(login_url='login/')
def cart(request): 
    cart_data=CartItem.objects.filter(cart__user=request.user)
    return render(request,'cart.html',{'cart_data':cart_data})

@login_required(login_url='login/')
def checkout(request): 
    cart_data=CartItem.objects.filter(cart__user=request.user)
    tot=0
    for cart in cart_data:
        tot+=cart.totprice
    return render(request,'checkout.html',{'cart_data':cart_data,'tot':tot})

@login_required(login_url='login/')
def order(request): 
    cartitem=CartItem.objects.filter(cart__user=request.user)
    for item in cartitem:
        Order.objects.create(cartitem=CartItem.objects.get(id=item.id))
    return redirect(reverse('index'))


    