from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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




