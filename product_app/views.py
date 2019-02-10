from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Productlar
from django.contrib.auth.decorators import login_required
from .forms import *

def login_page_data():
    return {
        "login_form": LoginForm()
    }

def baseindexview(request):
    if request.user.is_authenticated:
        return redirect("list_product")
    context = login_page_data()
    return render(request, "login.html", context)



def login_view(request):
    if request.method == "POST":
        context = login_page_data()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("list_product")
            else:
                context["message"] = "username or password invalid !"
                return render(request, "login.html", context)
        else:
            context["login_form"] = form
            return render(request, "login.html", context)
    else:
        return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")




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