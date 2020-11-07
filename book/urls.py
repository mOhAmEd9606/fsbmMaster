from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^Books/$',views.Etudiant,name="Etudiant"),
    url(r'^Books/$',views.BooksFrontEndpage,name="BooksFrontEndpage"),
    url(r'^Book=(?P<slug>.*)/$',views.booksDetail,name="books"),
    url(r'^AdminBooks/$',views.booksBackList,name="booksBackList"),
     url(r'^AddBooks/$',views.booksBackadd,name="booksBackadd"),

     ]
