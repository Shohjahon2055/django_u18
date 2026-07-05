from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'title'
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            'category_id',
            'title',
            'price',
            'description',
            'image'

        ]
