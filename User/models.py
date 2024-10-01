from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField('Birhday', null=True)


    REQUIRED_FIELDS = []