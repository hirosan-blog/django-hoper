from django.views.generic import View
from django.shortcuts import render
from .models import Hoper
# Create your views here.

class IndexView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/index.html')

class AboutView(View):
  def get(self,request,*args,**kwargs):
    hoper_data = Hoper.objects.all()
    if hoper_data.exists():
            hoper_data = hoper_data.order_by("-id")[0]
    return render(request,'app/about.html',
    {"hoper_data" : hoper_data})

class TeacherView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/teacher.html')
    
class PlanView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/plan.html')

class SignUpView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/sign_up.html')

class QuestionView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/question.html')