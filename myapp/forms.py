from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from . models import Customer

class LoginForm(AuthenticationForm):
    username =UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =['username','email','password1','password2']


class PasswordResetForm(PasswordChangeForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields =['name','city','number']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control', 'pattern':"[98][0-9]{9}"}),
            'city' :forms.TextInput(attrs={'class':'form-control'}),
        }

