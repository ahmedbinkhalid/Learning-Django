# here i am importing the path from django.urls
from django.urls import path
# here i import views from . means from same directory or i can also replace . with members
from . import views

urlpatterns = [
    path('members/', views.members, name= 'members')
]