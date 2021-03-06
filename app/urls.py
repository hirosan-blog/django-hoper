from django.urls import path
from app import views

urlpatterns = [
  path('',views.IndexView.as_view(),name="index"),
  path('about/',views.AboutView.as_view(),name="about"),
  path('teacher/',views.TeacherView.as_view(),name="teacher"),
  path('plan/',views.PlanView.as_view(),name="plan"),
  path('question/',views.QuestionView.as_view(),name="question"),
  path('contact/', views.ContactView.as_view(), name='contact'),
  path('thanks/', views.ThanksView.as_view(), name='thanks'),
  path('law/', views.LawView.as_view(), name='law'),
  path('privacy/', views.PrivacyView.as_view(), name='privacy'),
  path('use/', views.UseView.as_view(), name='use'),
  path('line/', views.LineView.as_view(), name='line'),
]