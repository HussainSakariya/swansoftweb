from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import widgets

from .models import MyUser

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Password"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Password Confirmation"}))

    class Meta:
        model = MyUser
        fields = ('email','password1' ,'password2' ,'mo_number','address')

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':"Email"}),
            'mo_number':forms.TextInput(attrs={'class':'form-control','placeholder':"Mo Number"}),
            'address':forms.Textarea(attrs={'placeholder':'Address','class':'form-control','rows':'3'})
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

