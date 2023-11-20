
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name=""),
    path('my-register', views.register, name="my-register"),
    path('my-login', views.Login, name = "my-login"),
    path('my-logout', views.logout, name= "my-logout"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('create-record', views.create_record, name="create-record"),
    path('my-back',views.back, name="my-back"),
    # Adding dynamic paths
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    path('update/<int:pk>', views.update_record, name="update"),
    
]