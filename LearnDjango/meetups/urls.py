from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    
    path('meetups/', views.index, name='all-meetups'), # our-domain.com/meetups
    path('meetups/success', views.confirm_registration, name = 'confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),# our-domain.com/meetups/ <dynamic-path-segment>
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)