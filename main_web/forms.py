# from dataclasses import fields
# from pyexpat import model

# from django.forms import ModelForm
# from dataclasses import fields
# from inspect import Attribute
# from random import choices
# from select import select
# from tkinter import Widget
# from tkinter.tix import INTEGER
# from xml.dom.minidom import Attr
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate 
from django import forms
from django.utils.safestring import mark_safe

Uni_choices=[
   ('OTHER','OTHER'),
   ('GIKI','GIKI'),
]

class Newtaskform(forms.Form):
   task=forms.CharField(label="new task")
  # priority=forms.IntegerField(label="pri",min_value=1,max_value=7)
 

class Signupform(UserCreationForm):
      first_name=forms.CharField(max_length=200,     label="First Name")
      
      last_name=forms.CharField(max_length=200,label="Last Name") 
      
      email = forms.EmailField()
      
      university = forms.CharField(
         max_length=30,
         widget=forms.TextInput(attrs={'id': 'uni-input-field',})
         )
     

      apl_for=forms.CharField(widget=forms.RadioSelect(choices=[("Mentor","Mentor"),("Mentee","Mentee")]))

      reg_no=forms.IntegerField()


      year=forms.IntegerField(widget=forms.Select(choices=[("1","1st Year"),("2","2nd Year"),("3","3r Year"),("4","4th Year")]))
      
      faculty=forms.CharField(widget=forms.Select(choices=[
         ("FCSE","FCSE"),
         ("FME","FME"),
         ("FEE","FEE"),
         ("FCVE","FCVE"),
         ("MGS","MGS"),
         ("FMCE","FMCE"),
      ]))

      class Meta:
         model=User
         fields=["username","first_name","last_name","email","password1","password2","university","reg_no","year","faculty","apl_for"]
         

class Signinform(UserCreationForm):
   class Meta:
      model=User
      fields=["username","password"]

course_choices = [
   ('CS101','CS101'),
   ('CS131','CS131'),

]

class best_courses_form():
   course_1 = forms.CharField(widget=forms.Select(choices=[course_choices]))   

   course_2 = forms.CharField(widget=forms.Select(choices=[course_choices]))   

   course_3 = forms.CharField(widget=forms.Select(choices=[course_choices]))   


