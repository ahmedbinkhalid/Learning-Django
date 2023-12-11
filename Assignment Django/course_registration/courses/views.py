from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, FormView
from .models import Course
from . forms import CourseRegisterForm, CourseDropForm

class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'

class CourseAddView(CreateView):
    model = Course
    fields = ['course_id', 'course_title', 'instructor', 'capacity']
    template_name = 'courses/add.html'

    def get_success_url(self):
        return reverse_lazy('courses:list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete.html'

    def get_success_url(self):
        return reverse_lazy('courses:list')

class CourseRegisterView(FormView):
    form_class = CourseRegisterForm
    template_name = 'courses/register.html'

    def get_success_url(self):
        return reverse_lazy('courses:list')

    def form_valid(self, form):
        course = get_object_or_404(Course, pk=form.cleaned_data['course_id'])
        if course.open_seats > 0:
            course.open_seats -= 1
            course.save()
            return super().form_valid(form)
        else:
            raise ValidationError('Course is full')

class CourseDropView(FormView):
    form_class = CourseDropForm
    template_name = 'courses/drop.html'

    def get_success_url(self):
        return reverse_lazy('courses:list')

    def form_valid(self, form):
        course = get_object_or_404(Course, pk=form.cleaned_data['course_id'])
        if course.open_seats < course.capacity:
            course.open_seats += 1
            course.save()
            return super().form_valid(form)
        else:
            raise ValidationError('Course is already empty')
