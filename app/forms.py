from django import forms

class UserForm(forms.Form):
  lastname = forms.CharField(label="姓名",max_length=10)
  firstname = forms.CharField(label="名前",max_length=20)
  address = forms.CharField(label="住所",max_length=30)
  team = forms.CharField(label="所属チーム",max_length=30)
  number = forms.CharField(label="電話番号",max_length=20)
  mail = forms.CharField(label="メール",max_length=30)