from django.shortcuts import render
# Here i am importing the HttpResponse from django.http
from django.http import HttpResponse
from django.template import loader
from .models import Members

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
