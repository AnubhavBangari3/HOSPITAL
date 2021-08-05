from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"), 
    path('book',Appointment,name="book"),
    path("update/<str:id>",updateAppointment,name="update"),
    path("delete/<str:id>",cancelAppointment,name="cancel"),
    path('about',about,name="about")
]
