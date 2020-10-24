from django.views.generic import View
from django.shortcuts import render
from .models import About
# Create your views here.

class IndexView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'app/index.html')

class AboutView(View):
  def get(self,request,*args,**kwargs):
    about_data = About.objects.all()
    if about_data.exists():
            about_data = about_data.order_by("-id")[0]
    return render(request,'app/about.html',
    {"about_data" : about_data})

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
    
    def post(self, request, *args, **kwargs):
        form = form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")

            return redirect('thanks')

        return render(request, 'app/contact.html', {
            'form': form
        })



class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')