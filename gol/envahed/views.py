from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from .permissions import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Ostad, Dars, Student
from .forms import OstadForm, DarsForm, StudentForm
import requests
from django.shortcuts import render


@permission_classes([IsTeacher]) 
def edit_dars(request , dars_id):
     dars = Dars.objects.get(id=dars_id)
     if request.method == 'POST':
         form = DarsForm(request.POST , instance= dars)
         if form.is_valid():
             form.save()
             return render(request , 'envahed/edit_dars.html' , {'form':form})

@permission_classes([IsStudent])
def show_dars(request):
    my_sudent = Student.objects.get(user=request.user)
    my_dars = my_sudent.dars.all()
    return render(request , 'envahed/show_dars.html' , {'dars':my_dars})




@permission_classes([IsTeacher]) 
def delet_dars(request , dars_id):
    dars = Dars.objects.get(id=dars_id)
    if request.method == 'DELETE':
        form = DarsForm(request.POST , instance= dars)
        if form.is_valid():
            form.delete()
            return render(request,)
            
def show_all_dars(request):
    dars = Dars.objects.all()
    return render(request , 'envahed/show_all_dars.html' , {'dars':dars})

