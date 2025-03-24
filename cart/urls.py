from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("cart/detail", views.CartDetailView.as_view(), name='cart_detail'),
    path("cart/add/<int:pk>", views.CartAddView.as_view(), name='cart_add'),
    path("cart/delete/<str:id>", views.CartDeleteView.as_view(), name='cart_delete'),
    path("cart/order/<int:pk>", views.OrderDetailView.as_view(), name='order_detail'),
    path("cart/order/create", views.OrderCreationView.as_view(), name='order_create'),
    path("cart/order/applydiscount/<int:pk>", views.ApplyDiscountView.as_view(), name='apply_discount'),
    path("cart/order/sendrequest/<int:pk>", views.SendRequestView.as_view(), name='send_request'),
    path("cart/order/verify", views.VerifyView.as_view(), name='verify_request'),
]
