from django.db import models
import datetime
# Create your models here.

    
class Diseases(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name)
choices=(
    ('Cardiologists','Cardiologists'),('Immunologists','Immunologists'),('Ophthalmologists','Ophthalmologists'),
    ('Dermatologists','Dermatologists'),('Endocrinologists','Endocrinologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
    ('Physicians','Physicians'),('Gastroenterologists','Gastroenterologists'),
    ('Hematologists','Hematologists'),
    ('Infectious Disease Specialists','Infectious Disease Specialists'),
    ('Nephrologists','Nephrologists'),('Neurologists','Neurologists'),('Gynecologists','Gynecologists'))
class Doctors(models.Model):
    name=models.CharField(max_length=255)
    
    intro=models.TextField(blank=True)
    specialization=models.CharField(max_length=255,choices=choices,blank=True,null=True)
    diseases=models.ManyToManyField(Diseases)
    
    def __str__(self):
        return str(self.name)
    
choices=(('Male','Male'),('Female','Female'),('Others','Others'))
TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )
class Patients(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=255,choices=choices)
    disease=models.ForeignKey(Diseases,on_delete=models.CASCADE,related_name="problem")   
    doctor_name=models.ForeignKey(Doctors,on_delete=models.CASCADE,related_name="doctor_name")
    fees=models.IntegerField(default=500)
    
    from_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    timeslot = models.IntegerField(choices=TIMESLOT_LIST,blank=True,null=True)
    date = models.DateField(help_text="YYYY-MM-DD",blank=True,null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
    
