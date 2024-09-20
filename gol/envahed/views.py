from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.shortcuts import render
from .models import *
from .forms import *
def edit_dars(request , dars_id):
     dars = Dars.objects.get(id=dars_id)
     if request.method == 'POST':
         form = DarsForm(request.POST , instance= dars)
         if form.is_valid():
             form.save()
             return 