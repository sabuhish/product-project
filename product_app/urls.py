from django.urls import path
from . import views

urlpatterns = [
    path("", views.baseindexview, name="home"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path("product/", views.list_product, name="list_product"),
    # path("upload_photo", views.upload_pic, name="upload_pic"),
    path("search", views.searchposts, name="search"),
    path("new_product/", views.create_product, name="create_product"),
    path("update/<int:id>/", views.update_product, name="update_product"),
    path("delete/<int:id>/", views.delete_product, name="delete_product")
]
