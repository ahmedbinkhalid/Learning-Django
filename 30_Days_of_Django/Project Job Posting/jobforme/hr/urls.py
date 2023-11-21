
from django.urls import path
from . import views

urlpatterns = [
    path('hr-dash', views.hrHome, name="hr-dash"),
]