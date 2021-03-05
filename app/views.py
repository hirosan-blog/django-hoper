from django.views.generic import View
from django.shortcuts import render
from .models import About,TopMessage,Teacher,Plan,PlanContentsCategory,QuestionCategory,Question
from django.template.loader import render_to_string

class IndexView(View):
  def get(self,request,*args,**kwargs):
    top_messages = TopMessage.objects.all()
    if top_messages:
      top_message = top_messages[0]
    else:
      top_message = ""
    return render(request,'app/index.html',{"top_message":top_message})

class AboutView(View):
  def get(self,request,*args,**kwargs):
    about_data = About.objects.all()
    if about_data.exists():
            about_data = about_data.order_by("-id")[0]
    return render(request,'app/about.html',
    {"about_data" : about_data})

class TeacherView(View):
  def get(self,request,*args,**kwargs):
    teacher_data = Teacher.objects.order_by("-id")
    teacher = teacher_data[0]
    return render(request,'app/teacher.html',{"teacher":teacher})
    
class PlanView(View):
  def get(self,request,*args,**kwargs):
    plan_data = Plan.objects.order_by("id")
    plan_list = PlanContentsCategory.objects.order_by("id")
    pl = plan_data[0]
    return render(request,'app/plan.html',{
      "plan_data":plan_data,
      "plan_list":plan_list,
      })

class SignUpView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/sign_up.html')

class QuestionView(View):
  def get(self,request,*args,**kwargs):
    question_title = QuestionCategory.objects.order_by("id")
    question_set = Question.objects.all()
    return render(request,'app/question.html',{
      "question_title":question_title,
      "question_set":question_set,
      })

class LawView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/law.html')

class PrivacyView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/privacy.html')

class UseView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/use.html')

class LineView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/line.html')






from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import ContactForm
# from .models import Profile, Work, Experience, Education, Software, Technical
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'app/contact.html', {
            'form': form
        })
    
    # def post(self, request, *args, **kwargs):
    #     form = form = ContactForm(request.POST or None)

    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']
    #         domain = 'hoper-baseball.com'
    #         context = {
    #                 'protocol': 'https' if self.request.is_secure() else 'http',
    #                 'name':name,
    #                 'email':email,
    #                 'domain': domain,
    #                 'message':message
    #         }

    #         body = render_to_string('app/mail_template/contact.txt', context)
    #         subject = render_to_string('app/mail_template/subject.txt', context)
    #         to_list = [email]
    #         bcc_list = [settings.EMAIL_HOST_USER]

    #         try:
    #             message = EmailMessage(subject=subject, body=body, to=to_list, bcc=bcc_list)
    #             message.send()
    #         except BadHeaderError:
    #             return HttpResponse("無効なヘッダが検出されました。")

    #         return redirect('thanks')

    #     return render(request, 'app/contact.html', {
    #         'form': form
    #     })



class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')