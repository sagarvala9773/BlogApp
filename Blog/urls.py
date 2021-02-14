from django.urls import path,register_converter
from . import views



urlpatterns = [
    
    path('',views.log_in,name="login"),
    path('signup/',views.sign_up,name="signup"),
    path('conformation/',views.conform,name="conformation"),
    path('profile/',views.userprofile,name="profile"),
]
