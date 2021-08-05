from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PatientForm
from .models import Diseases,Doctors,Patients

# Create your views here.
def home(request):
    form=PatientForm()
    doctors=Doctors.objects.all()
    if request.method == "POST":
        form=PatientForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('home')
        else:
            pass
    else:
        form=PatientForm()
        
        context={"form":form,"doctors":doctors}
        
    
    return render(request,"Patient/index.html",context)

def Appointment(request):
    patients=Patients.objects.all()
    # d1=patients.from_date
    # d2=patients.till_date
    # x=d2-d1
    context={"patients":patients}
    return render(request,"Patient/appointments.html",context)

def updateAppointment(request,id):
    patient=Patients.objects.get(id=id)
    form=PatientForm(instance=patient)
    if request.method == "POST":
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            
        return redirect('book')
    context={
        "form": form,
    }
    return render(request,"Patient/update_booking.html",context)
def cancelAppointment(request,id):
    patient=Patients.objects.get(id=id)
    if request.method == "POST":
        patient.delete()
        
        return redirect("book")
    context={
        "patient": patient
    }
    return render(request,"Patient/delete.html",context) 

def about(request):
    
    return render(request,"Patient/about.html")

    
        
    
        
