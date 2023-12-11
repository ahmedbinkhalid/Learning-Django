from django import forms
from .models import Course

class CourseRegisterForm(forms.Form):
    course_id = forms.CharField(label='Course ID', max_length=255)

class CourseDropForm(forms.Form):
    course_id = forms.CharField(label='Course ID', max_length=255)