from django.urls import path
from .views import CourseListView, CourseAddView, CourseDeleteView, CourseRegisterView, CourseDropView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('add/', CourseAddView.as_view(), name='add'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='delete'),
    path('<int:pk>/register/', CourseRegisterView.as_view(), name='register'),
    path('<int:pk>/drop/', CourseDropView.as_view(), name='drop'),
]