from django.shortcuts import render
from .models import Ostad, Dars, Student
from .forms import OstadForm, DarsForm, StudentForm
import requests


def add_dars(request):
    form = DarsForm()
    if request.method == "POST":
        form = DarsForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"envahed/add_dars.html", {"form": form})  
      
def show_dars(request):
    form = DarsForm()
    my_student = Student.objects.get(user = request.user)
    dars = my_student.dars.all()
    return render(request,"envahed/show_dars.html", {"dars": dars})

