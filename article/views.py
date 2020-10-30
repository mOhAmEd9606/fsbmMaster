from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from .forms import *
from etudiant.models import *
import string
import random
# Create your views here.

"""___-Cat-___"""





    
    
      
def Articlepage(request):
    context = {
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'ArticlePop':Article.objects.all().order_by('-show')[:6],
        'articles' : Article.objects.filter(),
        'Filiernavebar': Filier.objects.all().order_by('pk'),

    }
    responce = render(request,'front/ArticlePage.html',context)
   
    return responce
def Catpage(request,catt):
    context = {
        'catname':catt,
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'ArticlePop':Article.objects.all().order_by('-show')[:5],
        'articles' : Article.objects.filter(cat=cat),
        'Filiernavebar': Filier.objects.all().order_by('pk'),

    }
    responce = render(request,'front/CatPage.html',context)
    return responce
def ArticleDetail(request,pk):
    Upcount=Article.objects.get(pk=pk)
    Upcount.show = Upcount.show + 1
    Upcount.save()
    
    context = {
        'Tags': Tags.objects.all(),
        'Links':Links.objects.all(),
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'articles' : Article.objects.filter(pk=pk),
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'ArticlePop':Article.objects.all().order_by('-show')[:3],
        }

    responce = render(request,'front/articleDetail.html',context)
    return responce


    # Add
    # Del










"""
Article 
    manage
    delete
Catagury
    ,,
Links
    ,,
Tags
    ,,
"""
def ArticleManager(request):

    context = {
        'Articles':Article.objects.all(),
        'MEDs':Article.objects.all(),
          #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    response = render(request,'back/Art/index.html',context)
    return response
def ArticleAdd(request):
    form=ArticleForm()
    if request.method == "POST":
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            artID=form.cleaned_data['cat']
            size=9
            chars=string.ascii_uppercase + string.digits
            RandId = ''.join(random.choice(chars) for _ in range(size))
            name = form.cleaned_data['name']
            catagury = Cat.objects.get(name=artID).name
            catId = Cat.objects.get(name=artID).pk
            form.save()
           
            count = len(Article.objects.filter(catID=catId , name=name))
            artCount = Cat.objects.get(name=artID)
            artCount.count = count
            artCount.save()
            mes = (' Created Succesfully ')
            messages.success(request, mes)
            return redirect('ArticleManager')
        else:
            mes = (' Form Not Created Succesfully ')
            messages.info(request, mes)
            return redirect('ArticleManager')

    context = {
        'form':form,
        'Articles':Article.objects.all(),
        'MEDs':Article.objects.all(),
          #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    response = render(request,'back/Art/Add.html',context)
    return response

def ArtDel(request, pk):

    order = Article.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        catid = order.catID
        modName = Cat.objects.get(pk=catid)
        count = len(Article.objects.filter(pk=pk))
        modName.count = count
        modName.save()
        name = order.name
        mes = (f' {name} Deleted Succesfully ')
        messages.success(request, mes)
        return redirect('ArticleManager') 
    context = {
        'item':order,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    return render(request,'back/Art/delete.html',context)

def CatManager(request):
    
    context = {
        'Articles':Article.objects.all(),
        'MEDs':Article.objects.all(),
          #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    response = render(request,'back/Art/cat.html',context)
    return response


def ArtPanelDetail(request,pk):
    context = {
        'Articles':Article.objects.filter(pk=pk)
    }
    return render(request,'back/Art/ArtPanelDetail.html',context)