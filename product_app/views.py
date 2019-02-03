from django.shortcuts import render, redirect
from product_app.models import Productlar
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .modules.users import *


@login_required(login_url="/")
def login(request):
    context= {}
    return render(request, "login.html", context)

def login_page(request):
    params = {
            
        }
    if request.POST.get('login_btn') == '1':
        Username = request.POST.get('Username','')
        Password = request.POST.get('Password','')
        user_id = get_user(Username,Password)
        if not user_id:
            params['error_msg'] = "Login or password is wrong"
        else :
            request.session['user'] = user_id
            return redirect('product/')
             

    return render(request,'login.html',params)

@login_required(login_url="/")
def list_product(request):
    products = Productlar.objects.all()
    return render(request, "product.html", {"products": products})


@login_required(login_url="/")
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("list_product")
    return render(request, "products-form.html", {"form": form})


@login_required(login_url="/")
def update_product(request, id):
    product = Productlar.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect("list_product")
    return render(request, "products-form.html", {"form":form, "product":product})

@login_required(login_url="/")
def delete_product(request, id):
    product = Productlar.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect("list_product")
    return render(request, "product-delete-confirm.html", {"product": product })