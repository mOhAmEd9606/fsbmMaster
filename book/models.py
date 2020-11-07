from __future__ import unicode_literals
from django.db import models
from article.models import *
from etudiant.models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User, Group, Permission
import string
import random
from django.utils.text import slugify

# Create your models here.
class Books(models.Model):
    PRODACT_CHOIS = (('Free','Free'),('Not_Free','Not_Free'))
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=200, null=True, choices=PRODACT_CHOIS) 
    price = models.FloatField(null=True, blank=True,default='00')   
    description = RichTextUploadingField()
    ecrivain = models.CharField(max_length=25, default='none')
    filier = models.ManyToManyField(Filier,  blank=True)
    cat = models.ManyToManyField(Cat,  blank=True)
    pic  = models.ImageField(upload_to="Books/Image",default="book.png", null=True, blank=True)
    pdf=models.FileField(upload_to="Books/Pdf" , max_length=200)
    show = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Books.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count) 
                has_slug = Books.objects.filter(slug=slug).exists()

            self.slug = slug
       
        super().save(*args, **kwargs)
    


 