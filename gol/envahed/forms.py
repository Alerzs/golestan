from django import forms
from .models import Ostad, Dars, Student

class OstadForm(forms.ModelForm):
    class Meta:
        model = Ostad
        fields ="__all__"

class DarsForm(forms.ModelForm):
    class Meta:
        model = Dars
        fields ="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ="__all__"