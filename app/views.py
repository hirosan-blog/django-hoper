from django.views.generic import View
from django.shortcuts import render
# from .models import Post
# Create your views here.

class IndexView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/index.html')

class AboutView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/about.html')

class TeacherView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/teacher.html')
    
class PlanView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/plan.html')