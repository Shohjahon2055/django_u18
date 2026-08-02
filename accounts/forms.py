from django import forms
from accounts.models import CustomUser,Role


class RegisterForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'last_name',
            'email',
            'phone',
            'password'
        ]
    def save(self, commit = True):
        username=self.cleaned_data.get('username')
        last_name=self.cleaned_data.get('last_name')
        email=self.cleaned_data.get('email')
        phone=self.cleaned_data.get('phone')
        password=self.cleaned_data.get('password')
        return CustomUser.objects.create_user(
            username=username,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
        )

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=150)

class RoleForm(forms.Form):
    username=forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        empty_label="-- User tanlang --"
    )
    role=forms.ChoiceField(
        choices=Role
    )

class ForgetPasswordForm(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)