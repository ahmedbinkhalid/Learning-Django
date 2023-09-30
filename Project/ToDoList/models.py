from django.db import models

# Create your models here.
class Weekplan(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    task = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
