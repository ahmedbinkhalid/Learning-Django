
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name=""),
    path('my-register', views.register, name="my-register"),
    path('my-login', views.Login, name = "my-login"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('create-record', views.create_record, name="create-record"),
    # Adding dynamic paths
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    
]