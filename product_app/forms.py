from django import forms
from .models import Productlar

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productlar
        fields = ["kod","adi", "qiymeti", "gram", "miqdari"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

