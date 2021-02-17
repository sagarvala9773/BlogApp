from django.urls import path,register_converter
from . import views



urlpatterns = [
    
    path('',views.log_in,name="login"),
    path('signup/',views.sign_up,name="signup"),
    path('logout',views.log_out,name="logout"),
    path('profile/',views.userprofile,name="profile"),
    path('changepassword/',views.change_password,name="changepassword"),
    path('showuser/<my_id>',views.show_user,name="showuser"),
    path('deleteuser/<int:my_id>',views.delete_user,name="deleteuser")
]
