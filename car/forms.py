from django import forms
from .models import Car,Phone,About
class CarForm(forms.Form):
    model=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Sarloxani kiriting...',
    }))
    price=forms.IntegerField()
    description=forms.CharField()


    def save(self):
        model=self.cleaned_data.get('model')
        price=self.cleaned_data.get('price')
        description=self.cleaned_data.get('description')
        image=self.cleaned_data.get('image')
        return Car.objects.create(
            model=model,
            price=price,
            description=description,

        )

    def clean_model(self):
        model=self.cleaned_data.get('model')
        if len(model)<3:
            raise forms.ValidationError("Mashina modeli kamida 3 ta harfdan iborat bolishi kerak")
        return model

    def clean_price(self):
        price=self.cleaned_data['price']
        if price<0:
            raise forms.ValidationError("Narx manfiy bolishi mumkin emas")
        return price

    def clean_description(self):
        nostandart='byd'
        description=self.cleaned_data['description']
        data=description.split(' ')
        data=[d.lower() for d in data]
        if nostandart in data:
            raise forms.ValidationError(f"Bizni sayt {nostandart} sozidan foydalanish mumkin emas")

        return description

    def clean(self):
        data=super().clean()
        model=self.data.get("model")
        if len(model)<4:
            raise forms.ValidationError("Mashina harfi kamida 2 harfdan iborat bolsin ")
        return data



class PhoneForm(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    price = forms.IntegerField()
    storage = forms.IntegerField(min_value=0)
    ram = forms.IntegerField(min_value=0)
    battery = forms.IntegerField(min_value=0)
    os = forms.CharField(max_length=100)
    release_date = forms.DateField()
    description = forms.CharField()


    def save(self):
        brand=self.cleaned_data.get('brand')
        model=self.cleaned_data.get('model')
        color=self.cleaned_data.get('color')
        price=self.cleaned_data.get('price')
        storage=self.cleaned_data.get('storage')
        ram=self.cleaned_data.get('ram')
        battery=self.cleaned_data.get('battery')
        os=self.cleaned_data.get('os')
        release_date=self.cleaned_data.get('release_date')
        description=self.cleaned_data.get('description')

        return Phone.objects.create(
            brand=brand,
            model=model,
            color=color,
            price=price,
            storage=storage,
            ram=ram,
            battery=battery,
            os=os,
            release_date=release_date,
            description=description,

        )


class CarEditForm(forms.ModelForm):
    class Meta:
        model=Car
        fields='__all__'


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'