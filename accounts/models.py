

from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.utils import get_expiry_date, get_code


class Role(models.TextChoices):
    ADMIN='Admin','admin'
    MANAGER='Manager','manager'
    READER='Reader','reader'

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15)
    role=models.CharField(choices=Role.choices,default=Role.READER,max_length=50)



class Code(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='codes')
    code=models.CharField(default=get_code)
    expire_data=models.DateTimeField(default=get_expiry_date)

