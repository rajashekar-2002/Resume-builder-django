from django.contrib import admin
from .models import User
from .models import Profile
from .models import Account
from .models import Experiance
from .models import SSLC
from .models import PUC
from .models import University
from .models import Project
from .models import Skill


# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=['user','password']
    
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display=['image','fname','lname','pnumber','zip','city','address','objective','declaration','user']
    
@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display=['email','linkdin','github','facebook','pinterest','user']

@admin.register(Experiance)
class AdminExperiance(admin.ModelAdmin):
    list_display=['exp','user']
    

@admin.register(SSLC)
class AdminSSLC(admin.ModelAdmin):
    list_display=['name','year','board','marks','user','institute']
    
@admin.register(PUC)
class AdminSSLC(admin.ModelAdmin):
    list_display=['name','year','board','marks','user','institute']
    
@admin.register(University)
class AdminSSLC(admin.ModelAdmin):
    list_display=['name','year','board','marks','user','institute']
    
    
@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display=['name','description','link','user']
    
    
@admin.register(Skill)
class AdminSkill(admin.ModelAdmin):
    list_display=['softskill','techskill','lang','user']
    

