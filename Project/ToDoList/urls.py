from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('ToDoList/', views.ToDoList , name = 'ToDoList'),

]

