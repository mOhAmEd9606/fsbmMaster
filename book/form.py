from django.forms import ModelForm,ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class BooksForm(ModelForm):
	class Meta:
		model = Books
		fields = ['title','status','cat','filier','price','ecrivain','description','pic','pdf']
		widgets = {
			'filier':forms.CheckboxSelectMultiple(),
            'cat':forms.CheckboxSelectMultiple(),
            
		}
	