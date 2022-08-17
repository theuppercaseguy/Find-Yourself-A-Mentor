from asyncio import tasks
from unicodedata import name
from django.urls import path,include
from . import views



app_name="mentor_links" #uniquly identifies these urls
urlpatterns = [
   # path("home_api",views.home_api,name="index"),
   # path("",views.home,name="home"),
   
   path("",views.home,name="home"),
   path("home",views.home,name="home"),
   path("signup",views.signup,name="signup"),
   path("signin",views.signin,name="signin"),
   path("signout",views.signout,name="signout"),
   path('superuser',views.dashboard,name="dashboard_super"),
   path('user',views.dashboard,name="dashboard_user"),
   
   path("uni",views.unis,name="uni"),
   path("about",views.about,name="about"),

   
   
   # #path("<str:name>", views.greet,name="greet"),  #adding a genral url
   

   # path("task",views.task,name="mentors"),
   # path("task",views.task,name="reviews"),



]