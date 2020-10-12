from django.urls import path
from app import views

urlpatterns = [
  path('',views.IndexView.as_view(),name="index"),
  path('about/',views.AboutView.as_view(),name="about"),
  path('teacher/',views.TeacherView.as_view(),name="teacher"),
  path('plan/',views.PlanView.as_view(),name="plan"),
]