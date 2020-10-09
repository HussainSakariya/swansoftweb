from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from .managers import MyUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings 
from django.core.mail import send_mail 

# Create your models here.

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    mo_number=models.CharField(max_length=10)
    address=models.TextField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mo_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Products(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    qty=models.IntegerField()
    proimg=models.ImageField(upload_to="merchant_app/product")

class Cart(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    totprice = models.FloatField(blank=True)

status_ch=(
    ('accecpt','Accept'),
    ('reject','Reject'),
)

class Order(models.Model):
    cartitem=models.ForeignKey(CartItem,on_delete=models.CASCADE)
    status=models.CharField(choices=status_ch,max_length=10)

@receiver(post_save,sender=Order)
def order_save(sender, instance,created,**kwargs):
    if(created==False):
        print("Updated",instance.cartitem.cart.user)  
        subject = 'Thank You For Shopping...'
        message = f'''Hi {instance.cartitem.cart.user}, thank you for Shopping.
        your order has {instance.status}.'''
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [instance.cartitem.cart.user.email, ] 
        send_mail( subject, message, email_from, recipient_list ) 


    