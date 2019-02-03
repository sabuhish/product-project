from django.urls import path
from .views import *

urlpatterns = [
    path("", login_page, name="login-page"),
    path("product/", list_product, name="list_product"),
    path("new_product/", create_product, name="create_product"),
    path("update/<int:id>/", update_product, name="update_product"),
    path("delete/<int:id>/", delete_product, name="delete_product")
]
