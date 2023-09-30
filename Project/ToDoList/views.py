from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):

    return render(request, 'todolist/index.html')

# def Weekplan(request):
#     myplan = Weekplan.objects.all().values()
#     template = loader.get_template('week-schedule.html')
#     context = {
#         'myplan' : myplan,
#           }
#     return HttpResponse(template.render(context, request))
    
