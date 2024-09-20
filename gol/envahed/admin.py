from django.contrib import admin 
from .models import  *
# Register your models here.
@admin.register (Ostad)
class OstadAdmin(admin.ModelAdmin): ...

@admin.register (Student)
class StudentAdmin(admin.ModelAdmin): ...

@admin.register (Dars)
class DarsAdmin(admin.ModelAdmin): ...


# Register your models here.
