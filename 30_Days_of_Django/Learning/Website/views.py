from django.shortcuts import render, HttpResponse, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

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
        
def dashboard(request):
    return render(request, 'Website/dashboard.html')



        



