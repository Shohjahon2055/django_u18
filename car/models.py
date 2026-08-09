from django.db import models

from accounts.models import CustomUser


# Create your models here.

class Car(models.Model):
    model=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.TextField()



class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    battery = models.PositiveIntegerField()
    os = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()


    def __str__(self):
        return f"{self.brand} {self.model}"

#
# class Product(models.Model):
#     title = models.CharField(max_length=150)
#     category = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()
#     brand = models.CharField(max_length=100)
#     barcode = models.CharField(max_length=50, unique=True)
#     in_stock = models.BooleanField(default=True)
#     created_at = models.DateField()
#     expire_date = models.DateField()
#     description = models.TextField()
#
#     def __str__(self):
#         return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    grade = models.PositiveIntegerField()
    birthday = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    likes=models.ManyToManyField(CustomUser, through='Like',related_name='likes_post')

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.about.title}"
