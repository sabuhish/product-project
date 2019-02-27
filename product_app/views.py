from django.shortcuts import render, redirect
from django.shortcuts import  HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

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
    if "q" in request.GET:
        query = request.GET.get("q")
        lookups = Q(kod__icontains=query) | Q(adi__icontains=query) | Q(gram__icontains=query)
        products = Productlar.objects.filter(lookups).distinct()
    
    paginator = Paginator(products, 5) # Show 2 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    if page:
        page_range = paginator.page_range[int(page) - 3 if int(page) > 3 else 0:int(page) + 3]
    else:
        page_range = paginator.page_range[0:3]
    return render(request, "product.html", {"products": products,"page_range":page_range})



@login_required(login_url="/")
def create_product(request):
    form = ProductForm(request.POST or None)
    form_1 = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
       
        if form.is_valid() and form_1.is_valid():
            product = form.save()
            image = form_1.save(commit=False)
            image.sekil = product
            image.save()
            messages.success(request, f'Deyisiklik qeyde alindi!')
            # obj = form.save()
            # obj.sas = 21
            # obj.save()
            return redirect("list_product")
    context = {
            'form': form,
            'form_1': form_1
        } 
    return render(request, "products-form.html", context)

# @login_required(login_url='/')
# def add_post_view(request):
#     if request.method == "POST":
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             context = {
#                 "posts": Post.objects.all()
#             }
#             return render(request, "list_product")
#     return render(request, "products-form.html", context)

@login_required(login_url="/")
def update_product(request, id):
    product = Productlar.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    form_1 = ImageForm(request.POST, request.FILES)

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



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(kod__icontains=query) | Q(adi__icontains=query) | Q(gram__icontains=query)

            results= Productlar.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

def upload_pic(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')