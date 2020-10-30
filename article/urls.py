from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Panel/Catagurys/$',views.CatManager,name="CatManager"),
    # url(r'^Panel/(?P<cat>.*)se/(?P<ArtId>.*)se/$',views._Art_Detail,name="_Art_Detail"),
    # url(r'^Panel/Cat:delete_(?P<pk>\d+)_/$',views.CatDel,name="CatDel"),
    # url(r'^Panel/Arts/(?P<artID>.*)/$',views.ArticleAdmin,name="ArticleAdmin"),
    url(r'^Panel/Art:delete_(?P<pk>\d+)_/$',views.ArtDel,name="ArtDel"),
    url(r'^Arts/$',views.Articlepage,name="Articlepage"),
    url(r'^Arts/(?P<pk>\d+)/$',views.ArticleDetail,name="ArticleDetail"),
    url(r'^Article/(?P<catt>.*)s/$',views.Catpage,name="Catpage"),



    url(r'^AdminArticle/$',views.ArticleManager,name='ArticleManager'),
    url(r'^CreatArticle/$',views.ArticleAdd,name='ArticleAdd'),
    url(r'^Article/(?P<_Artid>.*)/$',views.ArtPanelDetail,name='ArtPanelDetail'),

     ]
