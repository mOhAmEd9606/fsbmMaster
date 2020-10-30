from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User, Group, Permission
import string
import random


# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=400 , default="name")
    count = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Article(models.Model):
    name = models.CharField(max_length=400 , default="name")
    # artID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    cat = models.ForeignKey(Cat, null=True, on_delete= models.SET_NULL)
    catID = models.IntegerField(default=0)
    discripton = RichTextField()
    artbody = RichTextUploadingField()
    pic  = models.ImageField(upload_to="Article",default="art.png", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    writer = models.OneToOneField(User ,null=True, on_delete=models.SET_NULL)
    show = models.IntegerField(default=0)
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Links(models.Model):
    name = models.CharField(max_length=400 , default="name")
    Artname = models.ForeignKey(Article, null=True, on_delete= models.SET_NULL)
    artId = models.CharField(max_length=400 , default="artId")
    link = models.CharField(max_length=400 , default="link")
    def __str__(self):
        return self.name
class Tags(models.Model):
    name = models.CharField(max_length=400 , default="name")
    Artname = models.ForeignKey(Article, null=True, on_delete= models.SET_NULL)
    artId = models.CharField(max_length=400 , default="artId")
    def __str__(self):
        return self.name


