from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    
    is_private = models.BooleanField(default = True)
    phone = models.CharField(max_length = 30, default = "")
    nickname = models.CharField(max_length = 60, unique = True, default = "")