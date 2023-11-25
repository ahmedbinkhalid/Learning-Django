from django.shortcuts import render

# Create your views here.
def users_dashboard(request):
    return render(request, 'users/home.html')
