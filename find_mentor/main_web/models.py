
from asyncio import constants
from enum import unique
from pickle import FALSE
from xml.parsers.expat import model
from django.db import models

import django.contrib.auth.models  # importing authentable users table from posgresql, fyam_database

# Create your models here.

class University(models.Model):
   name=models.CharField(max_length=30)
   location=models.CharField(max_length=100)


class Gikians(models.Model):
   
   reg_no=models.IntegerField(primary_key=True )
  
   uni_id=models.ForeignKey(University,null=False,on_delete=models.CASCADE,to_field='id')
  
   username=models.CharField(max_length=50,unique=True,null=False)

   hash = models.CharField(max_length=200,unique=True)
   
   email=models.EmailField(unique=True)
   
   name=models.CharField(max_length=20)
   
   year=models.IntegerField(null=False)
   
   faculty=models.CharField(max_length=10)

   role = models.CharField(max_length=10)

   def __int__(self):
       return self.reg_no

class Giki_socities(models.Model):
   
   reg_no=models.ForeignKey(Gikians,on_delete=models.CASCADE,to_field='reg_no')
   
   socities = models.CharField(max_length=30)
   

class Giki_teams(models.Model):
   reg_no=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE,to_field='reg_no')
  
   teams = models.CharField(max_length=30)
   

class Mentor(models.Model):
   reg_no=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE)

   year=models.IntegerField(null=False)
 

class Mentees(models.Model):

   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE,null=False,related_name='reg_no_is')

   mentor_id=models.ForeignKey(Gikians,null=True,on_delete=models.CASCADE,to_field='reg_no',related_name='mentor_ids')
   
   year = models.IntegerField()


class Mentees_of_mentors(models.Model):
   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE)

   men_id=models.ForeignKey(Gikians,null=True,on_delete=models.CASCADE,to_field='reg_no',related_name='men_ids')
  

class Mentor_skills(models.Model):

   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE,to_field='reg_no')

   skills=models.CharField(max_length=40)

class Mentor_best_courses(models.Model):
   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE,to_field='reg_no')
   
   best_courses=models.CharField(max_length=40)


class Mentees_weak_courses(models.Model):
   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE,to_field='reg_no')

   weak_courses=models.CharField(max_length=40)

class Mentee_interests(models.Model):
   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE,to_field='reg_no')
  
   interests = models.CharField(max_length=40)
   id = models.AutoField(primary_key=True,null=False)
   












