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
from django.views import View
from forms import *
from .models import *
from django.http import HttpResponse


class Chose_Dars(LoginRequiredMixin,View):
    def get(self,request):
        forms = DarsForm()
        return render (request,"",{"form":forms})
    def post(self,request):
        forms = IdDars(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            student = Student.objects.get(user = request.user)
            student.dars(id = cd["id_dars"])
            student.save()
            return HttpResponse ("ok")


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

<<<<<<< HEAD
 
=======

>>>>>>> 4f837f05757e9c14e346cffdaa18c4cc83fc149a


@permission_classes([IsTeacher]) 
def delet_dars(request , dars_id):
    dars = Dars.objects.get(id=dars_id)
    if request.method == 'DELETE':
        form = DarsForm(request.POST , instance= dars)
        if form.is_valid():
            form.delete()
            return render(request,)
            
