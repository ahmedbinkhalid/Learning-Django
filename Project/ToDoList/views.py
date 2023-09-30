from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Weekplan
# Create your views here.
def ToDoList(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def Weekplan(request):
    myplan = Weekplan.objects.all().values()
    template = loader.get_template('week-schedule.html')
    context = {
        'myplan' : myplan,
          }
    return HttpResponse(template.render(context, request))
    
