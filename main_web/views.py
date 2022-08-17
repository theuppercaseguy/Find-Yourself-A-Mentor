
from django.shortcuts import render,redirect
from django.db import connection
from .forms import Signupform
from django.contrib.auth import login, authenticate,logout 
from django.contrib import  messages 




#     Create your views here.

def home(request):
   return render(request, "main_web/home.html")



def signup(request):

   form = Signupform()
   if request.method=="POST":
      form = Signupform(request.POST)
      
      if form.is_valid():
      
##################################################
         messages.success(request,"Account Created.")
         
         cursor = connection.cursor()
         try:
            cursor.execute("insert into main_web_gikians(reg_no,username,email,name,year,faculty,role,uni_id_id) values(%s,%s,%s,%s,%s,%s,%s,%s)",
            (form.data['reg_no'],form.data['username'],form.data['email'],
            form.data['first_name'] + form.data['last_name'],form.data['year'],form.data['faculty'],form.data['apl_for'],1,))
         
            connection.commit()
                  
         except Exception as e:
            cursor.close()


         form.save()

         return redirect("/signin")

      else:
         print(f"Account not Created.{ str(form.errors.as_text)}")
         messages.success(request,f"Account not Created.{ str(form.errors.items)}" )
        
         return redirect("/signup")

   else:
      form=Signupform()
   
   return render(request,"main_web/signup.html",{
      'form':form,
   })

def signin(request):
   
   if request.method=="POST": 
      username=request.POST['username']
      password=request.POST['password']
      
      user = authenticate(request,username=username,password=password)
       
      if user is not None:
         login(request, user)
         
         return redirect('/home')
         
      else:
         messages.success(request,"The UserName or Password was Incorrect.")
         return render(request,'registration/login.html')
  
   else:
      return render(request,"registration/login.html",{
      "status":"login" ,

      })

def signout(request):
   logout(request)
   return redirect("mentor_links:home")
      

def dashboard(request):
   c1 = connection.cursor()
   c2 = connection.cursor()
   c3 = connection.cursor()
   c4 = connection.cursor()
   c5 = connection.cursor()
   c6 = connection.cursor()
   c7 = connection.cursor()
   c8 = connection.cursor()
   c9 = connection.cursor()
   c10 = connection.cursor()
   c11 = connection.cursor()
   c12 = connection.cursor()
   c13 = connection.cursor()
   c14 = connection.cursor()
   c15 = connection.cursor()
   c16 = connection.cursor()
   
   try:
      c1.execute('select * from main_web_gikians', ['localhost'])
      c2.execute('select * from main_web_university',['localhost'])
      c3.execute('select * from main_web_giki_socities',['localhost'])
      c4.execute('select * from main_web_giki_teams',['localhost'])
      c5.execute('select * from main_web_mentor',['localhost'])
      c6.execute('select * from main_web_mentees_of_mentors',['localhost'])
      c7.execute('select * from main_web_mentor_skills',['localhost'])
      c8.execute('select * from main_web_mentor_best_courses',['localhost'])
      c9.execute('select * from main_web_mentees',['localhost'])
      c10.execute('select * from main_web_mentees_weak_courses',['localhost'])
      c11.execute('select * from main_web_mentee_interests',['localhost'])



      row1 = c1.fetchall()
      row2 = c2.fetchall() 
      row3 = c3.fetchall() 
      row4 = c4.fetchall() 
      row5 = c5.fetchall() 
      row6 = c6.fetchall() 
      row7 = c7.fetchall() 
      row8 = c8.fetchall() 
      row9 = c9.fetchall() 
      row10 = c10.fetchall() 
      row11 = c11.fetchall() 

   except Exception as e:
       c1.close()
       c2.close()
       c3.close()
       c4.close()
       c5.close()
       c6.close()
       c7.close()
       c8.close()
       c9.close()
       c10.close()
       c11.close()
      
   context = {
                "table1":row1,
                "table2":row2,
                "table3":row3,
                "table4":row4,
                "table5":row5,
                "table6":row6,
                "table7":row7,
                "table8":row8,
                "table9":row9,
                "table10":row10,
                "table11":row11,

       }


   user = request.user.username

   if request.user.is_superuser:

      print(f'{request.user.is_superuser} is super user')
      return render(request,'main_web/admin_dashboard.html',context)
      

   elif not request.user.is_superuser:

      try:
         c12.execute("select role from main_web_gikians where username = %s",(user,))
         print(user)
         row1 = c12.fetchone()
         
         print(f'role is:{row1}')
         connection.commit()
         
      except Exception as e:
         c12.close()
         print(f'exception is: {e}')
      
      if str.lower(row1[0]) == 'mentor':
         print("now")
##################################################
         if request.method=="POST":
            
            course_1 = request.POST['course_1']
            course_2 = request.POST['cours_2']
            course_3 = request.POST['course_3']

            team_1 = request.POST['team_1']
            team_2 = request.POST['team_2']
            team_3 = request.POST['team_3']
            
            socity_1 = request.POST['socity_1']
            socity_2 = request.POST['socity_2']
            socity_3 = request.POST['socity_3']

            skill_1 = request.POST['skill_1']
            skill_2 = request.POST['skill_2']
            skill_3 = request.POST['skill_3']

            # print(f'is123: {request.POST}')
            row13 = ''
            row14 = ''
            row15 = ''
            user = request.user.username
            print(f'user logged in is: {user}')

            try:


               c15.execute("""
               select main_web_gikians.reg_no as "gikians_reg_no",
		         main_web_gikians.name,main_web_gikians.year,main_web_gikians.faculty,
		         main_web_gikians.email
				
               from main_web_gikians

               where  	main_web_gikians.role = 'mentee' and

		         main_web_gikians.reg_no in (
                  select main_web_mentees_of_mentors.men_id_id from main_web_mentees_of_mentors, main_web_gikians
		            where main_web_gikians.username = %s
		            and main_web_gikians.reg_no = main_web_mentees_of_mentors.reg_id)
  
		         order by main_web_gikians.name;          
               
               """,(user,))
               row13 = c15.fetchall()
               print(f'query 13 is: {row13}')



               c14.execute('select main_web_gikians.reg_no from main_web_gikians where username = %s ',(request.user.username))
               
               reg_no = c14.fetchall() #reg_no
               


               c15.execute("insert into main_web_mentor_best_courses (best_courses,reg_id) values(%s,%s)"
               , (course_1,reg_no[0]))

               c15.execute("insert into main_web_mentor_best_courses (best_courses,reg_id) values(%s,%s)"
               , (course_2,reg_no[0]))
               
               c15.execute("insert into main_web_mentor_best_courses (best_courses,reg_id) values(%s,%s)"
               , (course_3,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_1,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_2,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_3,reg_no[0]))


               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_1,reg_no[0]))

               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_2,reg_no[0]))

               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_3,reg_no[0]))


               c15.execute("insert into main_web_mentor_skills (skills,reg_id) values(%s,%s)"
               , (skill_1,reg_no[0]))

               c15.execute("insert into main_web_mentor_skills (skills,reg_id) values(%s,%s)"
               , (skill_2,reg_no[0]))
            
         

               c15.execute("insert into main_web_mentor_skills (skills,reg_id) values(%s,%s)"
               , (skill_3,reg_no[0]))

               connection.commit()
          
            except Exception as e:
               
               c13.close()
               c14.close()
               c15.close()
               c16.close()


            print('mentor 1 login')
            # return redirect("/main_web/dashboard_user",{"mentee":row13,})
            return render(request,'main_web/user_dashboard_mentor.html',{
              "mentee":row13,
              "username":request.user.username,
             })
            
         else:
             return render(request,'main_web/user_dashboard_mentor.html',{"username":request.user.username,})
        
##################################################




      elif str.lower(row1[0]) == 'mentee':
         
         if request.method=="POST":
            
            course_1 = request.POST['course_1']
            course_2 = request.POST['cours_2']
            course_3 = request.POST['course_3']

            team_1 = request.POST['team_1']
            team_2 = request.POST['team_2']
            team_3 = request.POST['team_3']
            
            socity_1 = request.POST['socity_1']
            socity_2 = request.POST['socity_2']
            socity_3 = request.POST['socity_3']

            skill_1 = request.POST['skill_1']
            skill_2 = request.POST['skill_2']
            skill_3 = request.POST['skill_3']

            # print(f'is123: {request.POST}')
            row13 = ''
            row14 = ''
            row15 = ''
            user = request.user.username
            print(user)

            try:


               c14.execute('select main_web_gikians.reg_no from main_web_gikians where username = %s ',(request.user.username,))
              
               reg_no = c14.fetchall() #reg_no

               
               c13.execute("""select main_web_gikians.reg_no as "gikians_reg_no",
		         main_web_gikians.name,main_web_gikians.year,main_web_gikians.faculty,
		         main_web_gikians.email
				
               from main_web_gikians

               where main_web_gikians.role = 'mentor' and

		         main_web_gikians.reg_no in (
                  select main_web_mentees_of_mentors.reg_id from main_web_mentees_of_mentors, main_web_gikians
		            where main_web_gikians.username = %s
		            and main_web_gikians.reg_no = main_web_mentees_of_mentors.men_id_id)
  
		         order by main_web_gikians.name;          
               """,(request.user.username,))
               

               
               c15.execute("insert into main_web_mentees_weak_courses (weak_courses,reg_id) values(%s,%s)"
               , (course_1,reg_no[0]))

               c15.execute("insert into main_web_mentees_weak_courses (weak_courses,reg_id) values(%s,%s)"
               , (course_2,reg_no[0]))
               
               c15.execute("insert into main_web_mentees_weak_courses (weak_courses,reg_id) values(%s,%s)"
               , (course_3,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_1,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_2,reg_no[0]))

               c15.execute("insert into main_web_giki_teams (teams,reg_no_id) values(%s,%s)"
               , (team_3,reg_no[0]))


               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_1,reg_no[0]))

               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_2,reg_no[0]))

               c15.execute("insert into main_web_giki_socities (socities,reg_no_id) values(%s,%s)"
               , (socity_3,reg_no[0]))

               c15.execute("insert into main_web_mentee_interests (interests,reg_id) values(%s,%s)"
               , (skill_1,reg_no[0]))

               c15.execute("insert into main_web_mentee_interests (interests,reg_id) values(%s,%s)"
               , (skill_2,reg_no[0]))
            

               c15.execute("insert into main_web_mentee_interests (interests,reg_id) values(%s,%s)"
               , (skill_3,reg_no[0]))

               row13 = c13.fetchall()

               connection.commit()
          
            except Exception as e:
               c13.close()
               c14.close()
               c15.close()
               c16.close()

            return render(request,'main_web/user_dashboard_mentee.html',{"username":request.user.username,
              "mentee":row13,
             })
         else:
             return render(request,'main_web/user_dashboard_mentee.html',{
                  "username":request.user.username,
             })




         
      else:
         return render(request,'main_web/home.html')


def unis(request):
    return render(request, "main_web/uni.html")

  
def about(request):
    return render(request, "main_web/about.html")