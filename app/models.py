from django.conf import settings
from django.db import models

class Hoper(models.Model):
  vision_content = models.TextField("ビジョン文章")
  feature_content = models.TextField("特徴文章")
  student_content = models.TextField("生徒文章")
  action_content = models.TextField("活動報告文章")
  join_content = models.TextField("入会文章")


def __str__(self):
  return self.title