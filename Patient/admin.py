from django.contrib import admin
from .models import Diseases,Doctors,Patients
# Register your models here.

admin.site.register(Diseases)
admin.site.register(Doctors)
admin.site.register(Patients)
