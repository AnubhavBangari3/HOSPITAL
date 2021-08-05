from django import forms
from django.forms import ModelForm
from .models import Patients

class PatientForm(ModelForm):
    class Meta:
        model=Patients
        fields=('first_name','last_name','gender','disease','doctor_name','fees','timeslot','date',)
        
        
        
        