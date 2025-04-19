from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    is_landlord = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    
