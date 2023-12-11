# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import UserCreationForm, LoginForm, CreateRecordForm, UpdateRecordForm
# from django.contrib.auth.models import auth
# from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
# from . models import Record



# # Homepage

# def home(request):
#     return render(request, 'webapp/index.html')

# # Register a User

# def register(request):

#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("my-login")
#     context = {'form' : form}

#     return render(request, 'webapp/register.html', context=context)

# # Login a User

# def my_login(request):

#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request, data = request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print(username)

#             user = authenticate(request, username= username, password= password)
#             if user is not None:
#                 auth.login(request, user)
#                 request.user = user

#                 return redirect("dashboard")

#     context = {'form': form}
#     return render(request, 'webapp/my-login.html', context=context)


# # Singleton

# class RecordManager:
#     _instances = {}

#     def __new__(cls, user):
#         if user not in cls._instances:
#             cls._instances[user] = super(RecordManager, cls).__new__(cls)
#             # Add any initialization logic here
#         return cls._instances[user]

#     def get_records(self, user):
#         return Record.objects.filter(user=user)


# # Dashboard
# @login_required(login_url='my-login')
# def dashboard(request):
#     record_manager = RecordManager(request.user)
#     my_records = record_manager.get_records(request.user)
#     print(request.user)
#     context = {'records': my_records}
#     return render(request, 'webapp/dashboard.html', context=context)



# # # Dashboard
# # @login_required(login_url='my-login')
# # def dashboard(request):

# #     my_records = Record.objects.all()
# #     context = {'records' : my_records}

# #     return render(request, 'webapp/dashboard.html', context=context)

# # Logout a User

# def user_logout(request):

#     auth.logout(request)

#     return redirect("my-login")

# # Create a Record

# @login_required(login_url='my-login')
# def create_record(request):
#     form = CreateRecordForm
#     if request.method == "POST":
#         form = CreateRecordForm(request.POST)
#         if form.is_valid():
#             record = form.save(commit=False)
#             record.user = request.user
#             form.save()

#             return redirect("dashboard")
        
#     context= {'form': form}

#     return render(request, 'webapp/create-record.html', context=context)


# # Update a Record

# @login_required(login_url='my-login')
# def update_record(request, pk):
#     record = Record.objects.get(id=pk)
#     form = UpdateRecordForm(instance=record)
#     if request.method =='POST':
#         form = UpdateRecordForm(request.POST, instance=record)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard")
        
#     context = {'form': form}
#     return render(request, 'webapp/update-record.html', context=context)

# # View/Update a Singular Record

# @login_required(login_url='my-login')
# def singular_record(request, pk):

#     all_records = Record.objects.get(id=pk)
#     context = {'record': all_records}

#     return render(request, 'webapp/view-record.html', context=context)

# # Delete a Record

# @login_required(login_url='my-login')
# def delete_record(request, pk):
#     record = Record.objects.get(id=pk)
#     record.delete()

#     return redirect('dashboard')


# course/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Course

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses})

class CourseAddView(View):
    def get(self, request):
        return render(request, 'course_add.html')

    def post(self, request):
        course_id = request.POST.get('course_id')
        course_title = request.POST.get('course_title')
        instructor = request.POST.get('instructor')

        Course.objects.create(
            course_id=course_id,
            course_title=course_title,
            instructor=instructor
        )
        return redirect('course_list')

class CourseDeleteView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('course_list')

class CourseActionView(View):
    def post(self, request, pk, action):
        course = get_object_or_404(Course, pk=pk)

        if action == 'add':
            if course.open_seats > 0:
                course.open_seats -= 1
        elif action == 'drop':
            if course.open_seats < course.capacity:
                course.open_seats += 1

        course.save()
        return redirect('course_list')


    




