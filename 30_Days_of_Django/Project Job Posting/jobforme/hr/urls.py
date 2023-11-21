
from django.urls import path
from . import views

urlpatterns = [
    path('hr-dash', views.hrHome, name="hr-dash"),
    path('post-job', views.post_job, name="post-job"),
    path('candidate-view', views.candidate_view, name="candidate-view"),
]