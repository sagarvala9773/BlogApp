from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update<int:id>/',views.update_data,name='update'),
    path('delete<int:id>/',views.delete_data,name='delete'),,
