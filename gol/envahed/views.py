from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from forms import *
from .models import *


class Chose_Dars(LoginRequiredMixin,View):
    def get(self,request):
        forms = DarsForm()
        return render (request,"",{"form":forms})
    def post(self,request):
        forms = DarsForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            forms.save()
            student = Student.objects.get(user = request.user)




            
            return render (request,"",{"form":forms})




