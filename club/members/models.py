from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.IntegerField(null=True)
    date = models.DateField(null=True)