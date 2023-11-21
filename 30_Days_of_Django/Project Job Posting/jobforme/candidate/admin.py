from django.contrib import admin
from candidate import models
# Register your models here.

@admin.register(models.MyJobList)
class MyJoblistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','job', 'applied_date')

@admin.register(models.isSortList)
class isSortListAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'job', 'applied_date')