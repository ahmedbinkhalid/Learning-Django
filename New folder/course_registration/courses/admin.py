from django.contrib import admin
from courses.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_title', 'instructor', 'capacity', 'open_seats')
    search_fields = ('course_id', 'course_title', 'instructor')
    readonly_fields = ('open_seats',)

admin.site.register(Course, CourseAdmin)
