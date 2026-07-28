from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.TextChoices):
    ADMIN='Admin','admin'
    MANAGER='Manager','manager'
    READER='Reader','reader'

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15)
    role=models.CharField(choices=Role.choices,default=Role.READER,max_length=50)

