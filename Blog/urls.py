from django.urls import path,register_converter
from . import views



urlpatterns = [
    
    path('',views.log_in,name="login"),
    path('signup/',views.sign_up,name="signup"),
    path('logout',views.log_out,name="logout"),
    path('profile/',views.userprofile,name="profile"),
    path('changepassword/',views.change_password,name="changepassword"),
]
