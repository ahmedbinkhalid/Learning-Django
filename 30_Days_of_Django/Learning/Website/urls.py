
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name=""),
    path('my-register', views.register, name="my-register"),
    path('my-login', views.Login, name = "my-login"),
    path('dashboard', views.dashboard, name = "dashboard"),
]