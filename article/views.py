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
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

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
        'articles' : Article.objects.filter(cat=catt),
        'Filiernavebar': Filier.objects.all().order_by('pk'),

    }
    responce = render(request,'front/CatPage.html',context)
    return responce
def ArticleDetail(request,artID):
    Upcount=Article.objects.get(artID=artID)
    Upcount.show = Upcount.show + 1
    Upcount.save()
    
    context = {
        'Tags': Tags.objects.all(),
        'Links':Links.objects.all(),
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'articles' : Article.objects.filter(artID=artID),
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
            print("--------------------------------------------------------------------")
            print("Form iv valid not Saved!")
            name = form.cleaned_data['name']
            cat=form.cleaned_data['cat']
            print(cat)
            wir=form.cleaned_data['writer']
            discripton=form.cleaned_data['discripton']
            artbody=form.cleaned_data['artbody']
            pic=form.cleaned_data['pic']
            RandId=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            
            catagury = Cat.objects.get(name=cat).name
            catId = Cat.objects.get(name=cat).pk
            if len(Article.objects.filter(catID=catId ,name=name)) != 0 :
                mes = (f' {name } Was Created Befor ')
                messages.info(request, mes)
                return redirect('ArticleManager')
            else : 
                Arti = Article(name=name,discripton=discripton, artbody=artbody,artID=RandId,cat=cat,catID=catId,writer=wir,pic=pic)
                Arti.save()
                counte = len(Article.objects.filter(catID=catId))
                artCount = Cat.objects.get(name=catagury)
                artCount.count = counte
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
    ArticleID = order.artID
    orderLink = Links.objects.filter(artId=ArticleID)
    
    if request.method == "POST":
        order.delete()
        orderLink.delete()
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
        'orderLink':orderLink,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    return render(request,'back/Art/delete.html',context)

def CatManager(request):
    form = CatForm()
    if request.method == "POST":
        form=CatForm(request.POST)
        if form.is_valid():
            form.save()
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
    response = render(request,'back/Art/cat.html',context)
    return response

def tagsAdd(request):
    formTags=TagsForm()
    if request.method == "POST":
        formTags=TagsForm(request.POST)
        if formTags.is_valid():
            name=formTags.cleaned_data['name']
            if len(Tags.objects.filter(name=name)) != 0 :
                mes = (f'{name} Created Befor ')
                messages.info(request, mes)
                return redirect('tags' )
            else :
                formTags.save()
                mes = (' Created Succesfully ')
                messages.success(request, mes)
                return redirect('tags' )
    context = {'formTags':formTags}
    return render(request,'back/Art/tagsform.html',context)
def tags(request):
    context = {'Tags':Tags.objects.all()}
    return render(request,'back/Art/tags.html',context)

def ArtPanelDetail(request,ARTID):
   
    deleteId = Article.objects.get(artID=ARTID).pk

    context = {
       
        'd_Id':deleteId,
        'Articles':Article.objects.filter(artID=ARTID),
        'Tags':Tags.objects.filter(artId=ARTID),
        'Tagsss':len(Tags.objects.filter(artId=ARTID)),
         'Links':Links.objects.filter(artId=ARTID),
         'linksss': len(Links.objects.filter(artId=ARTID)),
    }
    return render(request,'back/Art/ArtPanelDetail.html',context)
def AddLink(request):
    formlincks=lincksForm()
    if request.method == "POST":
        formlincks=lincksForm(request.POST)
        if formlincks.is_valid():
            name=formlincks.cleaned_data['name']
            link=formlincks.cleaned_data['link']
            artname = formlincks.cleaned_data['artname']
            ART=Article.objects.get(name=artname)
            arrrr=ART.artID
            print("__________________________________________________________")
            print(arrrr)
            formlincks.save(commit=False)
            if len(Links.objects.filter(name=name,artId=arrrr)) != 0 :
                mes = (f'{name} Created Befor ')
                messages.info(request, mes)
                return redirect('ArtPanelDetail', arrrr )
            else :
                C=Links(name=name,artId=arrrr,link=link)
                C.save()
                mes = (' Created Succesfully ')
                messages.success(request, mes)
                return redirect('ArtPanelDetail', arrrr )
    context = {'formlincks':formlincks}
    return render(request,'back/Art/addLink.html',context)
"""-Delete Tags"""
def TagsDel(request, pk):
    order = Tags.objects.get(id=pk)

    order.delete()
    ARTID=order.artId
    name = order.name
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('ArtPanelDetail', ARTID)
def LinksDel(request, pk):
    order = Links.objects.get(id=pk)

    order.delete()
    ARTID=order.artId
    name = order.name
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('ArtPanelDetail', ARTID)