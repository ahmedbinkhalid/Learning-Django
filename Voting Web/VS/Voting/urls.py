from django.urls import path
from . import views
urlpatterns = [
    path('voting-dash', views.Voting_dashboard, name="voting-dash"),
]