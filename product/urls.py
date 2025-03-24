from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product_detail" ),
    path("product/navbar", views.NavbarPartialView.as_view(), name="navbar" ),
    path("product/list", views.ProductListView.as_view(), name="product_list" ),
]