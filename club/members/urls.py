# here i am importing the path from django.urls
from django.urls import path
# here i import views from . means from same directory or i can also replace . with members
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('members/', views.members, name= 'members'), 
    path('members/details/<int:id>', views.details, name = 'details'),
    path('register_members', views.register_members, name= 'register_members'),
    

]