from django.urls import path
from . import views
urlpatterns = [
    path('users-dash', views.users_dashboard, name="users-dash"),
]