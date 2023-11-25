from django.shortcuts import render

# Create your views here.

def hosting_dashboard(request):
    return render(request, 'Hosting/home.html')