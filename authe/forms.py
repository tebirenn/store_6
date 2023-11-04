from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import User

# class UserSignUpForm(forms.Form):
#     username = forms.CharField(
#         label='Имя пользователя',
#         widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
#     )
#     email = forms.EmailField(label='Почта')
#     first_name = forms.CharField(required=False, label='Имя')
#     last_name = forms.CharField(required=False, label='Фамилия')
#     password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput())

#     # class Meta:
#     #     widgets = {
#     #         'username': forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
#     #     }


class UserSignUpForm(forms.ModelForm): 
    # description = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password',)
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        } 


class UserSignInForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
