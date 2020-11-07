from django.forms import ModelForm,ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['name','cat','writer','discripton','artbody','tags','pic']
		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}
		

class CatForm(ModelForm):
	class Meta:
		model = Cat
		fields = ['name']
class lincksForm(ModelForm):
	class Meta:
		model = Links
		fields = ['name','artname','link']
class TagsForm(ModelForm):
	class Meta:
		model = Tags
		fields = ['name']
