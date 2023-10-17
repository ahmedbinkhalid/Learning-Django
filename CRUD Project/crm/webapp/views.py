from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm

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
            # return redirect()
    context = {'form' : form}

    return render(request, 'webapp/register.html', context=context)
