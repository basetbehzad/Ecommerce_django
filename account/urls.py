from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path('account/login', views.LoginUser.as_view(), name='user_login'),
    path('account/otp_login', views.OtpLoginView.as_view(), name='otp_login'),
    path('account/check_otp', views.CheckOtpView.as_view(), name='check_otp'),
    path('account/logout', views.user_logout, name='logout'),
    path('account/add/address', views.AddAddressView.as_view(), name='add_address'),
]