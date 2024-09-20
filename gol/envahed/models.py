from django.db import models
from django.contrib.auth.models import User




class Ostad(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

class Dars(models.Model):
    vahed = models.IntegerField()
    ostad = models.ForeignKey(Ostad ,on_delete=models.CASCADE)
    rooz = models.DateTimeField()
    cap = models.PositiveIntegerField()
    reshte = models.CharField(max_length=25)
    

class Student(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    reshte = models.CharField(max_length=20)
    dars = models.ManyToManyField(Dars)