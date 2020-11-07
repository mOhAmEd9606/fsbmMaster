from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
import string
import random
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from etudiant.models import *
from article.models import *
from .models import *
from .form import *

def booksDetail(request,slug):
    context = {
        'Books':Books.objects.get(slug=slug),
    }
    return render(request,'front/books/bookDownload.html',context)
def BooksFrontEndpage(request):
    context = {
        'Filiernavebar': Filier.objects.all().order_by('pk'),

        'Books':Books.objects.all().order_by('-pk'),
        'BooksPop':Books.objects.all().order_by('-show')[:6],

    }
    return render(request,'front/books/books.html',context)
def booksBackList(request):
    context = {
        'Books': Books.objects.all().order_by('pk'),
           #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    return render(request,'back/book/list.html',context)
def booksBackadd(request):
    form = BooksForm()
    if request.method == "POST":
        form = BooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booksBackList')
    context = {
        'form':form,
           #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    return render(request,'back/book/add.html',context)