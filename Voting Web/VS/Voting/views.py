from django.shortcuts import render

# Create your views here.
def Voting_dashboard(request):
    return render(request, 'Voting/home.html')
