from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Record(models.Model):

    first_name= models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(max_length= 50, blank=False)
    phone = PhoneNumberField(blank= False)
    address = models.CharField(max_length=500)
    city =models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

