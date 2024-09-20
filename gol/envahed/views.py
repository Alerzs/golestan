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
             return render(request, )


@permission_classes([IsTeacher]) 
def delet_dars(request , dars_id):
    dars = Dars.objects.get(id=dars_id)
    if request.method == 'DELETE':
        form = DarsForm(request.POST , instance= dars)
        if form.is_valid():
            form.delete()
            return render(request,)
            