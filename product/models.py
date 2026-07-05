from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='product',blank=True,null=True)