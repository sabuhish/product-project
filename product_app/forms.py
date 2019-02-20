from django import forms
from .models import Productlar, Images

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productlar
        fields = ["kod","adi","əyar", "qiymeti", "gram", "miqdari","məzənnə", "status", "publish_1"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

