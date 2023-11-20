from django.shortcuts import render, HttpResponse, redirect
from .forms import UserCreationForm, LoginForm, CreateRecord
from .forms import UpdateRecordForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record

# view for Home page
def home(request):
    return render(request, 'Website/index.html')

# View for Regiteration Page

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    context = {'form' : form}
    return render(request, 'Website/registeration.html', context = context) 

# View for User Login

def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form': form}
    return render(request, 'Website/login.html', context = context)
        
#  Creating Dashboard View
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'Website/dashboard.html', context=context)

# Creating Record View

def create_record(request):
    form = CreateRecord()
    if request.method == "POST":
        form = CreateRecord(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form':form}
    return render(request, 'Website/Create-Record.html', context=context)

# View for Viewing Records
@login_required(login_url='my-login')
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context={'record': all_records}
    return render(request, 'Website/View-Record.html', context=context)

#  Deleteing a Single Reocrd
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect('dashboard')

def back(req):
    return redirect('dashboard')

# Update Record View
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'Website/update-record.html', context=context)

# Logout Button
@login_required(login_url='my-login')
def logout(request):
    auth.logout(request)
    return redirect('my-login')






        



