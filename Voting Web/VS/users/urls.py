from django.urls import path
from . import views
urlpatterns = [
    path('', views.users_dashboard, name=""),
    path('register-host', views.register_host, name="register-host"),
    path('reg-voter', views.register_voter, name="reg-voter"),
    path('login-host', views.host_login, name="login-host"),
    path('login-voter', views.voter_login, name="login-voter"),
]