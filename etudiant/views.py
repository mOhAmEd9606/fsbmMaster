from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from .models import *
from article.models import *
from book.models import *
from django.contrib.auth.decorators import login_required
import datetime
from itertools import chain
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.contrib import messages
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import FileSystemStorage
mySearch=""

#"""___Coures___"""

def coureAdmin(request,modl,pk):
    formcoure = AddfCoureForm()
    # coure add 
    if request.method == "POST":
        formcoure = AddfCoureForm(request.POST, request.FILES)
        if formcoure.is_valid():
            name = formcoure.cleaned_data['name']
            pdf = formcoure.cleaned_data['pdf']
            module = Module.objects.get(nameUrl=modl,pk=pk).name
            moduleurl =Module.objects.get(nameUrl=modl,pk=pk).nameUrl
            filID =Module.objects.get(nameUrl=modl,pk=pk).filieriD
            print('-------------------------------------------------------------')
            print(module)
            print(moduleurl)
            print('-------------------------------------------------------------')
            word = len(Cours.objects.filter(name=name,module=module,filierID=filID))
            if word != 0 :
                mes = (f'{name} was created Befor ')
                messages.info(request, mes)
            else :
                formcoure.save(commit=False)
                semmesterID = Module.objects.get(nameUrl=modl,pk=pk).semmesteriD
                semmester = Semmester.objects.get(pk=semmesterID).name
                semmesterUrl = Semmester.objects.get(pk=semmesterID).nameUrl
                filierID = Semmester.objects.get(pk=semmesterID).filierId
                filier = Filier.objects.get(pk=filierID).name
                
                coreSave = Cours(name=name,pdf=pdf,module=module,moduleid=pk,semmester=semmester,semmesterID=semmesterID,semmesterUrl=semmesterUrl,filier=filier,filierID=filierID,moduleUrl=moduleurl)
                coreSave.save()
                count = len(Cours.objects.filter(moduleid=pk))
                modName=Module.objects.get(pk=pk)
                modName.ccount = count
                modName.save()
                mes = (f'{name} was created Soccesfully ')
                messages.success(request, mes)
        else:
            mes = ('Something is worren ')
            messages.warning(request, mes)

    modules = Module.objects.get(nameUrl=modl,pk=pk)
    mod = Module.objects.filter(nameUrl=modl,pk=pk)
    coure = Cours.objects.filter(moduleid=pk)
    context = {
        'formcoure':formcoure,
        'Modules':modules,
        'Coures':coure,
        'MEDs':mod,
        'md': modules,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    return render(request, 'back/coure/add.html',context)
def moduleDel(request, pk):

    order = Cours.objects.get(id=pk)
    if order.pdf:
        order.pdf.delete()
    order.delete()
    count = len(Cours.objects.filter(pk=pk))
    moduleid=order.moduleid
    modName=Module.objects.get(pk=moduleid)
    modName.ccount = count
    modName.save()
    name = order.name
    nameurl = order.moduleUrl
    oId = order.moduleid
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('coureAdmin',modl=nameurl,pk=oId)



#"""___TDs___"""

def TdsAdmin(request,modl,pk):
    print('-----------------defualt--------------------------------------------')
    print('>in function ')
    print('-------------------------------------------------------------')
    form = AddTdForm()
    # coure add 
    if request.method == "POST":
        print('---------------------------p----------------------------------')
        print(">POST")
        print('-------------------------------------------------------------')
        form = AddTdForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            pdf = form.cleaned_data['pdf']
            module = Module.objects.get(nameUrl=modl,pk=pk).name
            moduleurl =Module.objects.get(nameUrl=modl,pk=pk).nameUrl
            filID =Module.objects.get(nameUrl=modl,pk=pk).filieriD
            print('---------------------------k----------------------------------')
            print('>In form')
            print('-------------------------------------------------------------')
            if len(TD.objects.filter(name=name,module=module,filierID=filID)) != 0 :
                mes = (f'{name} was created Befor ')
                messages.info(request, mes)
            else :
                form.save(commit=False)
                semmesterID = Module.objects.get(nameUrl=modl,pk=pk).semmesteriD
                semmester = Semmester.objects.get(pk=semmesterID).name
                semmesterUrl = Semmester.objects.get(pk=semmesterID).nameUrl
                filierID = Semmester.objects.get(pk=semmesterID).filierId
                filier = Filier.objects.get(pk=filierID).name
                
                coreSave = TD(name=name,pdf=pdf,module=module,moduleid=pk,semmester=semmester,semmesterID=semmesterID,semmesterUrl=semmesterUrl,filier=filier,filierID=filierID,moduleUrl=moduleurl)
                coreSave.save()
                count = len(TD.objects.filter(moduleid=pk))
                modName=Module.objects.get(pk=pk)
                modName.Tdcount = count
                modName.save()
                mes = (f'{name} was created Soccesfully ')
                messages.success(request, mes)
        else:
            mes = ('Something is worren ')
            messages.info(request, mes)

    modules = Module.objects.get(nameUrl=modl,pk=pk)
    mod = Module.objects.filter(nameUrl=modl,pk=pk)
    td = TD.objects.filter(moduleid=pk)
    context = {
        'form':form,
        'Modules':modules,
        'TDs':td,
        'MEDs':mod,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    return render(request, 'back/td/add.html',context)
def tdDel(request, pk):

    order = TD.objects.get(id=pk)
    if order.pdf:
        order.pdf.delete()
    order.delete()
    count = len(TD.objects.filter(pk=pk))
    moduleid=order.moduleid
    modName=Module.objects.get(pk=moduleid)
    modName.Tdcount = count
    modName.save()
    name = order.name
    nameurl = order.moduleUrl
    oId = order.moduleid
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('TdsAdmin',modl=nameurl,pk=oId)   


#"""___TP___"""

@login_required(login_url='loginPage')
def TpsAdmin(request,modl,pk):
    print('-----------------defualt--------------------------------------------')
    print('>in function ')
    print('-------------------------------------------------------------')
    form = AddtpForm()
    # coure add 
    if request.method == "POST":
        print('---------------------------p----------------------------------')
        print(">POST")
        print('-------------------------------------------------------------')
        form = AddtpForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            pdf = form.cleaned_data['pdf']
            module = Module.objects.get(nameUrl=modl,pk=pk).name
            moduleurl =Module.objects.get(nameUrl=modl,pk=pk).nameUrl
            filID =Module.objects.get(nameUrl=modl,pk=pk).filieriD
            print('---------------------------k----------------------------------')
            print('>In form')
            print('-------------------------------------------------------------')
            if len(TP.objects.filter(name=name,module=module,filierID=filID)) != 0 :
                mes = (f'{name} was created Befor ')
                messages.info(request, mes)
            else :
                form.save(commit=False)
                semmesterID = Module.objects.get(nameUrl=modl,pk=pk).semmesteriD
                semmester = Semmester.objects.get(pk=semmesterID).name
                semmesterUrl = Semmester.objects.get(pk=semmesterID).nameUrl
                filierID = Semmester.objects.get(pk=semmesterID).filierId
                filier = Filier.objects.get(pk=filierID).name
                
                coreSave = TP(name=name,pdf=pdf,module=module,moduleid=pk,semmester=semmester,semmesterID=semmesterID,semmesterUrl=semmesterUrl,filier=filier,filierID=filierID,moduleUrl=moduleurl)
                coreSave.save()
                count = len(TP.objects.filter(moduleid=pk))
                modName=Module.objects.get(pk=pk)
                modName.tpcount = count
                modName.save()
                mes = (f'{name} was created Soccesfully ')
                messages.success(request, mes)
        else:
            mes = ('Something is worren ')
            messages.info(request, mes)

    modules = Module.objects.get(nameUrl=modl,pk=pk)
    mod = Module.objects.filter(nameUrl=modl,pk=pk)
    td = TP.objects.filter(moduleid=pk)
    context = {
        'form':form,
        'Modules':modules,
        'TDs':td,
        'MEDs':mod,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    return render(request,'back/tp/add.html',context)
@login_required(login_url='loginPage')
def tpDel(request, pk):
    order = TP.objects.get(id=pk)
    if order.pdf:
        order.pdf.delete()
    order.delete()
    count = len(TP.objects.filter(pk=pk))
    moduleid=order.moduleid
    modName=Module.objects.get(pk=moduleid)
    modName.tpcount = count
    modName.save()
    name = order.name
    nameurl = order.moduleUrl
    oId = order.moduleid
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('TpsAdmin',modl=nameurl,pk=oId)   

#"""___exam___"""
@login_required(login_url='loginPage')
def examsAdmin(request,modl,pk):
    form = AddexamForm()
    print('-----------------defualt--------------------------------------------')
    print('>in function ')
    print('-------------------------------------------------------------')
    form = AddexamForm()

    # coure add 
    if request.method == "POST":
        print('---------------------------p----------------------------------')
        print(">POST")
        print('-------------------------------------------------------------')
        form = AddexamForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            pdf = form.cleaned_data['pdf']
            module = Module.objects.get(nameUrl=modl,pk=pk).name
            moduleurl =Module.objects.get(nameUrl=modl,pk=pk).nameUrl
            filID =Module.objects.get(nameUrl=modl,pk=pk).filieriD
            print('---------------------------k----------------------------------')
            print('>In form')
            print('-------------------------------------------------------------')
            if len(Exam.objects.filter(name=name,module=module,filierID=filID)) != 0 :
                mes = (f'{name} was created Befor ')
                messages.info(request, mes)
            else :
                form.save(commit=False)
                semmesterID = Module.objects.get(nameUrl=modl,pk=pk).semmesteriD
                semmester = Semmester.objects.get(pk=semmesterID).name
                semmesterUrl = Semmester.objects.get(pk=semmesterID).nameUrl
                filierID = Semmester.objects.get(pk=semmesterID).filierId
                filier = Filier.objects.get(pk=filierID).name
                
                coreSave = Exam(name=name,pdf=pdf,module=module,moduleid=pk,semmester=semmester,semmesterID=semmesterID,semmesterUrl=semmesterUrl,filier=filier,filierID=filierID,moduleUrl=moduleurl)
                coreSave.save()
                count = len(Exam.objects.filter(moduleid=pk))
                modName=Module.objects.get(pk=pk)
                modName.ecount = count
                modName.save()
                mes = (f'{name} was created Soccesfully ')
                messages.success(request, mes)
        else:
            mes = ('Something is worren ')
            messages.info(request, mes)

    modules = Module.objects.get(nameUrl=modl,pk=pk)
    mod = Module.objects.filter(nameUrl=modl,pk=pk)
    Exams = Exam.objects.filter(moduleid=pk)
    context = {
        'form':form,
        'Modules':modules,
        'Exams':Exams,
        'MEDs':mod,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    return render(request,'back/exam/add.html',context)
@login_required(login_url='loginPage')
def examDel(request, pk):
    order = Exam.objects.get(id=pk)
    if order.pdf:
        order.pdf.delete()
    order.delete()
    count = len(Exam.objects.filter(pk=pk))
    moduleid=order.moduleid
    modName=Module.objects.get(pk=moduleid)
    modName.ecount = count
    modName.save()
    name = order.name
    nameurl = order.moduleUrl
    oId = order.moduleid
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('examsAdmin',modl=nameurl,pk=oId)      


"""__Front Etudiant__"""


def PhysiquePage(request):
    fil= Filier.objects.get(name="Physique").pk
    filiern= Filier.objects.get(name="Physique").name
    print(fil)
    context = {
        'Books': Books.objects.all(),
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Filiers': Filier.objects.filter(name=filiern),
        'Module': Module.objects.all(),
        # 'ModulePop': Module.objects.all().order_by('-show')[:2],
        'Semmesters': Semmester.objects.filter(filier=filiern).order_by('name'),
        'lastCours': Module.objects.filter(filier="Physique").order_by('-pk')[:4],
    }
    phy=Filier.objects.get(name="Physique")
    phy.show= phy.show + 1
    phy.save()
    return render(request,'front/physiquePage12.html',context)
def SearchPhysiquePage(request):
    if request.method == "POST":
        word = request.POST.get('search')
    print(word)
    context = {
        'Filier':Filier.objects.all() ,
        "physique":Module.objects.all() ,
    }

    return render(request,'front/searchPhysique.html',context)

def physiqueSemmester(request,sem,pk):
    fil=Filier.objects.get(name="Physique").name
    print(fil)
    print(sem)# S4/Electronique-de-base
    print('-------------------------------------------------------------------------')

    showSem = Semmester.objects.get(filier=fil,nameUrl=sem,pk=pk)
    semmesterid=showSem.pk
    semmestername=showSem.name
    seemm = showSem.purname
   


    showSem.show= showSem.show + 1
    showSem.save()



    context = {
        'semmestername':seemm,
        'semmester':seemm,
        'Filiernavebar': Filier.objects.all().order_by('pk'),
         'Parcoure':  Semmester.objects.filter(filier=fil,nameUrl=sem,pk=pk),
         'Filier': Filier.objects.filter(name="Physique"),
         'Modules': Module.objects.filter(semmesteriD=pk ,filier="Physique"),
         'ModulePop': Module.objects.filter(semmesteriD=pk ,filier="Physique").order_by('-show')[:3],
    }

    return render(request,'front/psemmester.html',context)

def physiqueModulePage(request,sem,modl):
    print('sem :'+sem)#S4
    print('modl :'+modl)#Electronique-de-base
    print('--------------------------------------------------------')
    nammm=Module.objects.get(nameUrl=modl,semmesterUrl=sem,filier='Physique').semmester
    print('Modulename :'+str(nammm))#Electronique-de-base
    print('--------------------------------------------------------')
    context = {
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Cours': Cours.objects.filter(moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
        'PopCours': Cours.objects.filter(semmesterUrl=sem,semmester=nammm).order_by('-pk')[:3],
        'Module': Module.objects.filter(nameUrl=modl,semmesterUrl=sem,semmester=nammm),
         'Semmester': Semmester.objects.filter(nameUrl=sem,name=nammm),
          'Filier': Filier.objects.filter(name='Physique'),
          'TraveuxDiriges':TD.objects.filter(moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'TraveuxDirigesLastAdd':TD.objects.filter(semmesterUrl=sem,semmester=nammm)[:3],
           'TraveuxPratique':TP.objects.filter(moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'TraveuxPratiqueLastAdd':TP.objects.filter(semmesterUrl=sem,semmester=nammm),
           'Exams':Exam.objects.filter(moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'ExamsLastAdd':Exam.objects.filter(semmesterUrl=sem,semmester=nammm),
    }
    phy=Module.objects.get(nameUrl=modl,semmesterUrl=sem,filier='Physique',semmester=nammm)
    pp = phy.show 
    phy.show= phy.show + 1
    phy.Lasshow = pp
    phy.save()

    return render(request,'front/pmodule.html',context)

"""--chimie--"""

def ChimiePage(request):
    fil= Filier.objects.get(name="Chimie").pk
    
    context = {
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Filiers': Filier.objects.filter(name = "Chimie"),
        'Module': Module.objects.all(),
        'Semmesters': Semmester.objects.filter(filier = fil),
        'lastCours': Module.objects.filter(filier="Chimie").order_by('-pk')[:4],
    }
    phy=Filier.objects.get(name="Chimie")
    phy.show= phy.show + 1
    phy.save()
    return render(request,'front/chimiePage.html',context)
def SearchChimiePage(request):
    if request.method == "POST":
        word = request.POST.get('search')
    print(word)
    context = {
        'Filier':Filier.objects.all() ,
        "Chimie":Module.objects.all() ,
    }

    return render(request,'front/searchChimie.html',context)

def ChimieSemmester(request,sem,pk):
    fil=Filier.objects.get(name="Chimie").pk
    print(fil)
    print(sem)# S4/Electronique-de-base
    print('-------------------------------------------------------------------------')

    showSem = Semmester.objects.get(filier=fil,nameUrl=sem,pk=pk)
    semmesterid=showSem.pk
    semmestername=showSem.name
    seemm = showSem.purname
   


    showSem.show= showSem.show + 1
    showSem.save()



    context = {
        'semmestername':seemm,
        'semmester':seemm,
        'Filiernavebar': Filier.objects.all().order_by('pk'),
         'Parcoure':  Semmester.objects.filter(filier=fil,nameUrl=sem,pk=pk),
         'Filier': Filier.objects.filter(name="Chimie"),
         'Modules': Module.objects.filter(semmesteriD=pk ,filier="Chimie"),
         'ModulePop': Module.objects.filter(semmesteriD=pk ,filier="Chimie").order_by('-show')[:3],
    }

    return render(request,'front/Csemmester.html',context)

def ChimieModulePage(request,sem,modl):
    print('sem :'+sem)#S4
    print('modl :'+modl)#Electronique-de-base
    print('--------------------------------------------------------')
    nammm=Module.objects.get(nameUrl=modl,semmesterUrl=sem,filier='Chimie').semmester
    fiii=Module.objects.get(nameUrl=modl,semmesterUrl=sem,filier='Chimie').filier
    print('semmester :'+str(nammm))#Electronique-de-base
    print('filier :'+str(fiii))#Electronique-de-base
    print('--------------------------------------------------------')
    context = {
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Cours': Cours.objects.filter(filier=fiii,moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
        'PopCours': Cours.objects.filter(semmesterUrl=sem,semmester=nammm).order_by('-pk')[:3],
        'Module': Module.objects.filter(nameUrl=modl,semmesterUrl=sem,semmester=nammm),
         'Semmester': Semmester.objects.filter(nameUrl=sem,name=nammm),
          'Filier': Filier.objects.filter(name='Chimie'),
          'TraveuxDiriges':TD.objects.filter(filier=fiii,moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'TraveuxDirigesLastAdd':TD.objects.filter(filier=fiii,semmesterUrl=sem,semmester=nammm)[:3],
           'TraveuxPratique':TP.objects.filter(filier=fiii,moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'TraveuxPratiqueLastAdd':TP.objects.filter(semmesterUrl=sem,semmester=nammm),
           'Exams':Exam.objects.filter(moduleUrl=modl,semmesterUrl=sem,semmester=nammm),
          'ExamsLastAdd':Exam.objects.filter(semmesterUrl=sem,semmester=nammm),
    }
    phy=Module.objects.get(nameUrl=modl,semmesterUrl=sem,filier='Chimie',semmester=nammm)
    phy.show= phy.show + 1
    phy.save()

    return render(request,'front/pmodule.html',context)


# search -----
def Search_MOdule(request):
    if request.method == "POST":
        word = request.POST.get('search')
        word=mySearch
        a = Module.objects.filter(filier="Chimie",name__contains=word)
        b = Module.objects.filter(filier="Chimie",semmester__contains=word)
        c = Module.objects.filter(filier="Chimie",parcoure__contains=word)
        mods = list(chain(a,b,c))
        mods = list(dict.fromkeys(mods))
        paginator = Paginator(mods,12)
        page = request.GET.get('page')
        try:
            mod = paginator.page(page)
        except EmptyPage:
            mod = paginator.page(paginator.num_pages)
        except PageNotAnInteger :
            mod = paginator.page(1)


    else:
        a = Module.objects.filter(filier="Chimie",name__contains=mySearch)
        b = Module.objects.filter(filier="Chimie",semmester__contains=mySearch)
        c = Module.objects.filter(filier="Chimie",parcoure__contains=mySearch)
        mod = list(chain(a,b,c))
        mod = list(dict.fromkeys(mod))

    context = {
        'word':word,
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Parcourenavebar': Parcoure.objects.all().order_by('semmester'),
        'Cours': Cours.objects.filter(filier="Chimie",),
        'Mod': mod,
        'ModulePop': Module.objects.filter(filier="Chimie",).order_by('-show')[:3],
         'Parcoure': Parcoure.objects.filter(filier="Chimie",),
         'Semmester': Semmester.objects.filter(filier="Chimie",),
          'Filier': Filier.objects.filter(name="Chimie"),
            # 'SEmmester': Semmester.objects.get(filier="Chimie",).name,

    }
    response = render(request,'front/search/Smodule.html',context)

    return response




#___Back End ___:
"""
filier List = { manager:Filier_List ; delete:delete_filier}
Semmester List = { manager:semmester_list ; delete:delete_Semmester}
Module List = {manager:Module_list ; delete:delete_Module}

_



"""
    # filier List
def panelFilier_List(request):
    #Add filier
    formFilier = AddfillierForm()
    if request.method == "POST":

        formFilier=AddfillierForm( request.POST,request.FILES)
        if formFilier.is_valid():
            name = formFilier.cleaned_data['name']
            if len(Filier.objects.filter(name=name)) != 0 :
                mes = (f'{name} was created Befor ')
                messages.info(request, mes)
                return redirect('filier')
            else :
                formFilier.save()
                mes = (f'{name} was created Soccesfully ')
                messages.success(request, mes)
                return redirect('filier')
        else :
            mes = ('was Not created')
            messages.error(request, mes)
            return redirect('filier')
   
    context = {
        'formFilier':formFilier,
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        'Filier':Filier.objects.all(),
    }
    response = render(request,'back/filier/index.html',context)
    return response
def delete_filier(request,pk):
    order = Filier.objects.get(pk=pk)
    filie= order.pk
    # semmesterdel=Semmester.objects.get(filierId=filie)
    # moduledel=Module.objects.get(filieriD=filie)
    print('--------------------------------------------------------------------')
    print(filie)
    # print(moduledel)
    if request.method == "POST":
        order.delete()

        mes = (' was Deleted Soccesfully ')
        messages.success(request, mes)
        return redirect('filier')

    context = {
        'item':order,
        #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    response=render(request,'back/filier/delete.html',context)
    return response
def semmester_list(request,pk):
    filierr=Filier.objects.get(pk=pk)
    filieerr=Filier.objects.filter(pk=pk)
    filier=filierr.name
    filierid=filierr.pk
    print('-----------------------------filierid---------------------------------------------')
    print(filier)
    semm = Semmester.objects.filter(filierId=pk)
    form = AddSemmesterForm()
    if request.method == "POST":
        form = AddSemmesterForm( request.POST)
        if form.is_valid():
            bname = form.cleaned_data['name']
            word = len(Semmester.objects.filter(name=bname,filier=filier))
            print('-----------------------------1111---------------------------------------------')
            print(word)
            print(id)
            if word != 0 :
                mes = (f'{bname} was created Befor ')
                messages.info(request, mes)
                return redirect('semmester',pk)
            else :
                Q_semmester= Semmester(name=bname,filier=filier)
                Q_semmester.save()
                

                filierID = Filier.objects.get(name=filier).pk
                SemName = Semmester.objects.get(name=bname,filier=filier)
                bb = SemName.name
                if len(bb) == 3:
                    purname = bb.replace('p','')
                    purname = purname.replace('c','')
                    purname = purname.replace('i','')
                else : 
                    purname=bb
                 
                nameUrl = purname.replace(' ','-')
                nameUrl = nameUrl.replace('é','e')
               
                SemName.nameUrl = nameUrl
                SemName.filierId = filierID

                purname = purname.replace('S','Semmester ')
                SemName.purname=purname
                SemName.save()


                count = len(Semmester.objects.filter(filierId=filierID))
                FilName=Filier.objects.get(pk=filierID)
                FilName.count = count
                FilName.save()

                mes = (f'{bname} was created Succesfully ')
                messages.success(request, mes)
                return redirect('semmester',pk)
        else :
            mes = 'something is worren'
            messages.error(request, mes)
            return redirect('semmester',pk)

    context = {
        'filiers':filieerr,
        'id':filierid,
        'form':form,
        'filier':filier,
        'SemmesterObj':semm,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
    }
    response = render(request,'back/semmester/index.html',context)
    return response
def delete_Semmester(request,pk):
    order = Semmester.objects.get(pk=pk)
    filie= order.pk
    bb=order.filierId
    # semmesterdel=Semmester.objects.get(filierId=filie)
    # moduledel=Module.objects.get(filieriD=filie)
    print('--------------------------------------------------------------------')
    print(filie)
    # print(moduledel)
    if request.method == "POST":
        order.delete()

        mes = (' Was Deleted Soccesfully ')
        messages.success(request, mes)
        return redirect('semmester',bb)

    context = {
        'item':order,
        'filierID':bb,
        #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        #
        }
    response=render(request,'back/semmester/delete.html',context)
    return response
def module_list(request,pk):
    Sm=Semmester.objects.get(pk=pk)
    Sm_name=Sm.name
    Sm_namhe=Sm.purname
    Sm_ID=Sm.pk
    Sm_filierID=Sm.filierId
    md=Module.objects.filter(semmesteriD=pk,filieriD=Sm_filierID)
    Modulle=Module.objects.filter(semmesteriD=pk,filieriD=Sm_filierID)
    form = AddModuleForm()
    if request.method == "POST":
        form = AddModuleForm( request.POST)
        if form.is_valid():
            bname = form.cleaned_data['name']
            bsemmester = Sm_name
            word = len(Module.objects.filter(name=bname,semmester=bsemmester))
            if word != 0 :
                mes = (f'{bname} was created Befor ')
                messages.info(request, mes)
                return redirect('module',pk)
            else :
                form.save(commit=False)
                
                # rempleair fields 
                semmesterID = Semmester.objects.get(name=bsemmester).pk
                semmester = Semmester.objects.get(name=bsemmester).name
                semmesterUrl = Semmester.objects.get(name=bsemmester).nameUrl
                filierr = Semmester.objects.get(name=bsemmester).filier
                filierID = Filier.objects.get(name=filierr).pk
                filier = Filier.objects.get(pk=filierID).name

                nameUrl = bname.replace(' ','-')
                nameUrl = nameUrl.replace('é','e')
                nameUrl = nameUrl.replace('è','e')
                moduSave = Module(
                    name=bname,
                    nameUrl=nameUrl,
                    semmester=semmester,
                    nameSem=str(nameUrl)+' &' +str(semmesterUrl),
                    semmesteriD=semmesterID,
                    filier=filier,
                    semmesterUrl=semmesterUrl,
                    filieriD=filierID ,
                    )
                moduSave.save()
                # makeing a counter
                count = len(Module.objects.filter(semmesteriD=semmesterID,filieriD=filierID))
                modName=Semmester.objects.get(pk=semmesterID)
                modName.count = count
                modName.save()
                
                mes = (f'{bname} was created Succesfully ')
                messages.success(request, mes)
                return redirect('module',pk)
        else :
            mes = 'something is worren'
            messages.warning(request, mes)
            return redirect('module',pk)

    context = {
        'ttitel':Sm_namhe,
        'id':Sm_ID,
        'form':form,
        'filier':Sm_name,
        'modulesd':Modulle,
        'md':md,
         #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),
        #
    }
    response = render(request,'back/module/index.html',context)
    return response
def delete_Module(request,pk):
    order = Module.objects.get(pk=pk)
    bb=order.filieriD
    # semmesterdel=Semmester.objects.get(filierId=filie)
    # moduledel=Module.objects.get(filieriD=filie)
   
    # print(moduledel)
    if request.method == "POST":
        order.delete()

        mes = (' Was Deleted Soccesfully ')
        messages.success(request, mes)
        return redirect('module',bb)

    context = {
        'item':order,
        'moduleId':bb,
        #
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('name'),      
        }
    response=render(request,'back/module/delete.html',context)
    return response




