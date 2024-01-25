
from django import forms
from .models import Student
class Studentform(forms.ModelForm):
    class Meta:
          model=Student
          fields=["name","nikname","age"]
          widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),

         'nikname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nikname'}),

          'age': forms.TextInput(attrs={'class': 'form-control'})
          }
          