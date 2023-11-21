from django.shortcuts import render, redirect
from .models import JobPost, CandidateApplication
from .forms import create_job

# Create your views here.
def hrHome(request):
    job_posts = JobPost.objects.all()
    context = {'jobposts': job_posts}

    return render(request, 'hr/hrdashboard.html', context=context)

def post_job(request):
    if request.method == 'POST':
        title= request.POST.get('job-title'),
        address= request.POST.get('address')
        companyName = request.POST.get('company-name')
        salaryLow= request.POST.get('salary-low')
        salaryHigh = request.POST.get('salary-high')
        lastdatetoapply = request.POST.get('last-date')
        post = JobPost(user = request.user, title = title, address = address, companyName = companyName,salaryLow=salaryLow, salaryHigh = salaryHigh, lastdatetoapply= lastdatetoapply )
        
        post.save()
    return render(request, 'hr/jobpost.html')

def candidate_view(request):
    job_applies = CandidateApplication.objects.all()
    context = {'jobapplys': 'job_applies'}

    return render(request, 'hr/candidate.html', context=context)

# def post_job(request):
#     form = create_job()
#     if request.method == 'POST':
#         form = create_job(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hr-dash')
#     context = {'form': form}

#     return render(request, 'hr/jobpost.html', context=context)