from django.db import models

# Create your models here.

class User(models.Model):
    user=models.EmailField(max_length=25,blank=False)
    password=models.CharField(max_length=250,blank=False)
    
    def check_user(email):
        try:
            user=User.objects.all().filter(user=email).first()
            return user
        except:
            return False
    
class Profile(models.Model):
    image=models.FileField(upload_to='attachments/uploads',blank=False)
    fname=models.CharField(max_length=20,blank=False)
    lname=models.CharField(max_length=20,blank=False)
    pnumber=models.IntegerField(blank=False)
    zip=models.IntegerField(blank=False)
    city=models.CharField(max_length=20,blank=False)
    address=models.CharField(max_length=50,blank=False)
    objective=models.TextField(blank=True,default=None)
    declaration=models.TextField(blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Account(models.Model):
    email=models.EmailField(max_length=50,blank=False)
    linkdin=models.CharField(max_length=25,blank=False)
    github=models.CharField(max_length=25,blank=False)
    facebook=models.CharField(max_length=25,blank=True,default=None)
    pinterest=models.CharField(max_length=25,blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Experiance(models.Model):
    exp=models.TextField(blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class SSLC(models.Model):
    name=models.CharField(max_length=50,blank=False)
    year=models.CharField(max_length=6,blank=False)
    board=models.CharField(max_length=25,blank=True)
    institute=models.CharField(max_length=25,blank=True,default=None)
    marks=models.CharField(blank=True,default=None,max_length=6)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class PUC(models.Model):
    name=models.CharField(max_length=50,blank=True,default=None)
    year=models.CharField(max_length=6,blank=True,default=None)
    institute=models.CharField(max_length=25,blank=True,default=None)
    board=models.CharField(max_length=25,blank=True,default=None)
    marks=models.CharField(blank=True,default=None,max_length=6)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class University(models.Model):
    name=models.CharField(max_length=50,blank=True,default=None)
    year=models.CharField(max_length=6,blank=True,default=None)
    institute=models.CharField(max_length=25,blank=True,default=None)
    board=models.CharField(max_length=25,blank=True,default=None)
    marks=models.CharField(blank=True,default=None,max_length=6)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Project(models.Model):
    name=models.CharField(max_length=25,blank=False)
    description=models.TextField(blank=False)
    link=models.CharField(max_length=90,blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Skill(models.Model):
    softskill=models.TextField(blank=False,default=None)
    techskill=models.TextField(blank=True,default=None)
    lang=models.TextField(blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
       
    
    