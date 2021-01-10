from django.contrib import admin
from .models import About,TopMessage,Teacher,Plan,PlanContentsCategory,QuestionCategory,Question

# Register your models here.
admin.site.register(About)
admin.site.register(TopMessage)
admin.site.register(Teacher)
admin.site.register(Plan)
admin.site.register(PlanContentsCategory)
admin.site.register(QuestionCategory)
admin.site.register(Question)