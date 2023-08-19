from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.resume,name='resume'),
    path('form/',views.form,name='form'),
    path('resume/',views.final,name='final'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
  
]
