from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    capacity = models.IntegerField(default=30)
    open_seats = models.IntegerField(default=30)

    def __str__(self):
        return self.course_title
