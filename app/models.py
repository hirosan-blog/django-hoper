from django.conf import settings
from django.db import models

class User(models.Model):
  lastname = models.CharField("姓名",max_length=10)
  firstname = models.CharField("名前",max_length=20)
  address = models.CharField("住所",max_length=30)
  team = models.CharField("所属チーム",max_length=30)
  number = models.CharField("電話番号",max_length=20)
  mail = models.CharField("メール",max_length=30)


def __str__(self):
  return self.title