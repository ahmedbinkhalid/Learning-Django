from django.shortcuts import render, redirect
from .models import JobPost, CandidateApplication, SelectedCandidateJob
from .forms import create_job

# Create your views here.
def hrHome(request):
    job_posts = JobPost.objects.all()
    context = {'jobposts': job_posts}

    return render(request, 'hr/hrdashboard.html', context=context)

def post_job(request):
    msg = None
    if request.method == 'POST':
        title= request.POST.get('job-title'),
        address= request.POST.get('address')
        companyName = request.POST.get('company-name')
        salaryLow= request.POST.get('salary-low')
        salaryHigh = request.POST.get('salary-high')
        msg = "Job added successfully"
        lastdatetoapply = request.POST.get('last-date')
        post = JobPost(user = request.user, title = title, address = address, companyName = companyName, lastdatetoapply= lastdatetoapply )
        
        post.save()
    return render(request, 'hr/jobpost.html', {'msg':'msg'})

def candidate_view(request,id):
    if JobPost.objects.filter(id=id).exists():
        jobpost = JobPost.objects.get(id=id)
        jobapplys = CandidateApplication.objects.filter(job=jobpost)
        print(jobapplys)
        selectedCandidate = SelectedCandidateJob.objects.filter(job=jobpost)
        print(selectedCandidate)
        jobpost.applycount += 1
        return render(request,'hr/candidate.html',{'jobapplys':jobapplys,'jobpost':jobpost,'selectedCandidate':SelectedCandidateJob})
    else:
        return render('hr-dash') 
    
    # # job_applies = CandidateApplication.objects.all(id = pk)
    # # context = {'job_applies': 'job_applies'}
    # print(pk)

    # return render(request, 'hr/candidate.html')

# def post_job(request):
#     form = create_job()
#     if request.method == 'POST':
#         form = create_job(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hr-dash')
#     context = {'form': form}

#     return render(request, 'hr/jobpost.html', context=context)