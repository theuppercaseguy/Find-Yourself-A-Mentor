from django.contrib import admin



from .models import Gikians,University,Giki_socities,Giki_teams,Mentee_interests,Mentees_weak_courses,Mentees_of_mentors,Mentor_best_courses,Mentor_skills,Mentees,Mentor

# Register your models here.

class Gikian_admin(admin.ModelAdmin):
   list_display=(
      'reg_no','role','username','hash','email','name','year','faculty','uni_id_id'
   )

class University_admin(admin.ModelAdmin):
   list_display = ('id','name','location')
   
class Skills_admin(admin.ModelAdmin):
   list_display= ('id','reg_id','skills')

class MBS_admin(admin.ModelAdmin):
   list_display= ('id','reg_id','best_courses')

class Mentor_admin(admin.ModelAdmin):
   list_display= ('id','reg_no_id','year')

class MOM_admin(admin.ModelAdmin):
   list_display= ('id','reg_id','men_id_id')

class Mentees_admin(admin.ModelAdmin):
   list_display= ('id','reg_id','mentor_id_id','year',)

class MWC_admin(admin.ModelAdmin):
   list_display= ('id','weak_courses','reg_id')

class MI_admin(admin.ModelAdmin):
   list_display= ('id','reg_id','interests')

class Teams_admin(admin.ModelAdmin):
   list_display= ('id','reg_no_id','teams')

class Socities_admin(admin.ModelAdmin):
   list_display= ('id','reg_no_id','socities')


admin.site.register(Gikians,Gikian_admin)
admin.site.register(University,University_admin)
admin.site.register(Giki_socities,Socities_admin)
admin.site.register(Giki_teams,Teams_admin)
admin.site.register(Mentee_interests,MI_admin)
admin.site.register(Mentees_weak_courses,MWC_admin)
admin.site.register(Mentees_of_mentors,MOM_admin)
admin.site.register(Mentor_best_courses,MBS_admin)
admin.site.register(Mentor_skills,Skills_admin)
admin.site.register(Mentees,Mentees_admin)
admin.site.register(Mentor,Mentor_admin)



