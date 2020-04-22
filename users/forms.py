from django.db import models
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import AbstractUser


class UserCreationForm(UserCreationForm):
    email = models.EmailField(unique=True)

    class Meta:
        model = User
        fields = ('username', 'email')

