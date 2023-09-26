from django.shortcuts import render, redirect
# Here i am importing the HttpResponse from django.http
from django.http import HttpResponse
from django.template import loader
from .models import Members
from .forms import Membership

# Create your views here.
# Here i defined a funtion with request parameter
def members(request):
    # returning the HttpResponse again the request mention in funtion members
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    context ={
        'mymembers' : mymembers,
    }

    return HttpResponse(template.render(context, request))
def details(request, id):
    mymembers = Members.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# def register_members(request):
#     if request.method == 'POST':
#         form = Membership(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Registered Successfuly')
#         else:
#          form = Membership()
    
#     return render(request, 'register_member.html', {'form': form})
def register_members(request):
    form = Membership()  # Create an instance of the form
    if request.method == 'POST':
        form = Membership(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    return render(request, 'register_member.html', {'form': form})

