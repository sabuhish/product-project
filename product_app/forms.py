from django import forms
from .models import Productlar, Images
from django.forms import ModelForm, Textarea, TextInput, CharField
from django.utils.translation import ugettext_lazy as _

class ProductForm(ModelForm):
    class Meta:
        model = Productlar
        fields = ["kod","adi","eyar", "alis_qiymeti", "satis_qiymeti", "gram", "miqdari","mezenne", "status", "publish_1"]
        labels ={
            "kod" :"Məhsulun Kodu",
            "adi": "Məhuslun Adi",
            "eyar": "Əyar",
            "alis_qiymeti": "Alış Qiyməti",
            "satis_qiymeti": "Satış Qiyməti",
            "status": "Hal-hazırdakı Statusu",
            "publish_1": "Tarix",
            "mezenne": "Məzənnə",
            "gram": "Qram"
        }
        # help_texts ={
        #     "kod": "sadasdasd"
        # }
        widgets = {
            "kod": TextInput(attrs={"placeholder": "Etiket kodu.."}),
            "adi": TextInput(attrs={"placeholder": "qızıl, briliant ve sayrə.."}),
            "eyar": TextInput(attrs={"placeholder": "585, 560"}),
            "alis_qiymeti": TextInput(attrs={"placeholder": "məs: 240 AZN (240 yazsan yetərdir)"}),
            "satis_qiymeti": TextInput(attrs={"placeholder": "məs: 290 "}),
            "gram": TextInput(attrs={"placeholder": "50qr, 80qr"}),
            "mezenne": TextInput(attrs={"placeholder": "ex: 1.70"}),
            
        }
        error_messages = {
            "kod":{
            "required" : "Bu alanı qeyd edin.",
            "invalid"  : "Xeta bas verdi"


            },
            'adi': {
                'max_length': "250 den artiq simvol qebul olunmur",
                "required" : "Mehsulun adini qeyd edin.",

            },
            "eyar":{
                "invalid"  : "Kesr olmayan reqem daxil edin"
                
            },
            "alis_qiymeti":{
                "invalid"  : "Reqem daxil edin.",
                "required" : "Alış qiymətini daxil edin.",

            },
            "satis_qiymeti":{
                "invalid"  : "Reqem daxil edin.",
                "required" : "Satış qiymətini daxil edin.",

            },
            "gram":{
            "invalid"  : "Reqem daxil edin."
            },
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

