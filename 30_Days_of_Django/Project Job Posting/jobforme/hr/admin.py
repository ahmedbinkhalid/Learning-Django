from django.contrib import admin
from . models import Hr, JobPost, CandidateApplication, SelectedCandidateJob
# Register your models here.
admin.site.register(Hr)
admin.site.register(JobPost)
admin.site.register(CandidateApplication)
admin.site.register(SelectedCandidateJob)

# @admin.register(models.Hr)

# class HrAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user')

# class JobPostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'title', 'address', 'companyName', 'salaryLow', 'SalaryHigh', 'applycount', 'lastdatetoapply')

# @admin.register(models.CandidateApplication)
# class CandidateApplicationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'job', 'passingyear', 'yearofExp', 'resume', 'status')
