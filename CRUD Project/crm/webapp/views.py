from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib. auth import authenticate



# Homepage

def home(request):
    return render(request, 'webapp/index.html')

# Register a User

def register(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'form' : form}

    return render(request, 'webapp/register.html', context=context)

# Login a User

def my_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password= password)
            if user is not None:
                auth.login(request, user)

                # return redirect("")

    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

# Logout a User

def user_logout(request):

    auth.logout(request)

    return redirect("my-login")



