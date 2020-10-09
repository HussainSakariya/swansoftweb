from django.db import models
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, mo_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not mo_number:
            raise ValueError('Users must have an Mobile Number')

        user = self.model(
            email=self.normalize_email(email),
            mo_number=mo_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mo_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            mo_number=mo_number,
            password=password,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
