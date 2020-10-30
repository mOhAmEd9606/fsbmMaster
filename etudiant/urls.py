from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^Etudiant/$',views.Etudiant,name="Etudiant"),
      url(r'^Physique/$',views.PhysiquePage,name="PhysiquePage"),
      url(r'^Physique/(?P<sem>.*)-ID!(?P<pk>\d+)/$',views.physiqueSemmester,name="physiqueSemmester"),
      url(r'^Physique/(?P<sem>.*)/(?P<modl>.*)/$',views.physiqueModulePage,name="physiqueModulePage"),
      url(r'^Physique-Search_/$',views.SearchPhysiquePage,name="SearchPhysiquePage"),
      url(r'^Physique/search/$',views.Search_MOdule,name="Search_MOdule"),

       url(r'^Chimie/$',views.ChimiePage,name="ChimiePage"),
      url(r'^Chimie/(?P<sem>.*)-ID!(?P<pk>\d+)/$',views.ChimieSemmester,name="ChimieSemmester"),
      url(r'^Chimie/(?P<sem>.*)/(?P<modl>.*)/$',views.ChimieModulePage,name="ChimieModulePage"),
      url(r'^Chimie-Search_/$',views.SearchChimiePage,name="SearchChimiePage"),
      url(r'^Chimie/search/$',views.Search_MOdule,name="Search_MOdule"),

        #___Filier
        url(r'^Panel/filier$',views.panelFilier_List,name="filier"),
        url(r'^Panel/filierDelete-pk:(?P<pk>\d+)/$',views.delete_filier, name="delete_filier"),
    
    
        # __Semmester 
       url(r'^Panel/Admin(?P<pk>\d+)/$',views.semmester_list, name="semmester"),
        url(r'^Panel/semmesterDelete-pk:(?P<pk>\d+)/$',views.delete_Semmester, name="delete_Semmester"),
   
    #     #__Module
          url(r'^Panel/adminModule(?P<pk>\d+)/$',views.module_list, name="module"),
        url(r'^Panel/moduleDelete-pk:(?P<pk>\d+)/$',views.delete_Module, name="delete_Module"),


      url(r'^Panel/CoureManageName:/(?P<modl>.*)-(?P<pk>\d+)/$',views.coureAdmin,name="coureAdmin"),
      url(r'^Panel/Coure:delete(?P<pk>\d+)/$',views.moduleDel,name="moduleDel"),

      url(r'^Panel/TdsManageName:/(?P<modl>.*)-(?P<pk>\d+)/$',views.TdsAdmin,name="TdsAdmin"),
      url(r'^Panel/td:delete_(?P<pk>\d+)_/$',views.tdDel,name="tdDel"),


       url(r'^Panel/TpsManageName:/(?P<modl>.*)-(?P<pk>\d+)/$',views.TpsAdmin,name="TpsAdmin"),
      url(r'^Panel/tp:delete_(?P<pk>\d+)_/$',views.tpDel,name="tpDel"),
   
      url(r'^Panel/ExamsManageName:/(?P<modl>.*)-(?P<pk>\d+)/$',views.examsAdmin,name="examsAdmin"),
      url(r'^Panel/exam:delete_(?P<pk>\d+)_/$',views.examDel,name="examDel"),
    
]
