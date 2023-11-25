from django.urls import path
from . import views
urlpatterns = [
    path('hosting-dash', views.hosting_dashboard, name="hosting-dash"),
]