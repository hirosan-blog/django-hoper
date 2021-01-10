from django.conf import settings
from django.db import models

class About(models.Model):
  vision_content = models.TextField("ビジョン文章")
  feature_content = models.TextField("特徴文章")
  student_content = models.TextField("生徒文章")
  action_content = models.TextField("活動報告文章")
  join_content = models.TextField("入会文章")

  def __str__(self):
    return self.vision_content

class TopMessage(models.Model):
  content = models.TextField("First View 文章 ")

  def __str__(self):
    return self.content

class Teacher(models.Model):
  think = models.TextField("思い")
  history = models.TextField("経歴")
  profile = models.TextField("プロフィール")
  private = models.TextField("プライベート")

  def __str__(self):
      return self.think
class Plan(models.Model):
  name = models.CharField("ブラン名",max_length=50)
  explanation = models.TextField("プラン説明")
  price = models.IntegerField("プラン価格",default=0)

  def __str__(self):
      return self.name

class PlanContentsCategory(models.Model):
    parent = models.ForeignKey(Plan, on_delete=models.CASCADE)
    name = models.CharField("プラン内容", max_length=200)

    def __str__(self):
        return self.name

class QuestionCategory(models.Model):
    name = models.CharField("質問カテゴリ", max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
  parent = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
  question = models.TextField("質問内容")
  answer = models.TextField("回答")

  def __str__(self):
      return self.question