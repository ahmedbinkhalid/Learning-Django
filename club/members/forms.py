from django import forms
from .models import Members

class Membership(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['first_name', 'last_name', 'phone']