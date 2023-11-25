from django.shortcuts import render

# Create your views here.
def users_dashboard(request):
    return render(request, 'users/Register-as.html')

def register_host(request):
    return render(request, 'users/Register-host.html')

def register_voter(request):
    return render(request, 'users/Register-Voter.html')

def host_login(request):
    return render(request, 'users/Login-Host.html')

def voter_login(request):
    return render(request, 'users/Login-Voter.html')
