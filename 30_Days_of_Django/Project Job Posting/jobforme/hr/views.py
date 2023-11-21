from django.shortcuts import render

# Create your views here.
def hrHome(request):
    return render(request, 'hr/hrdashboard.html')