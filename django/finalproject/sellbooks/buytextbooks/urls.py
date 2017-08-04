from django.conf.urls import url
from . import views

app_name = "books"

urlpatterns = [
    #/buytextbooks/
    url(r'^$', views.home, name='home'),#views.index,name = 'index'

    #/buytextbooks/detailtextbook.html/3(id or pk)/
    url(r'^detailtextbook.html/(?P<pk>[0-9]+)/$', views.TextbookDetailView.as_view(), name = 'detailtextbook'),

    #/buytextbooks/detailprepbook.html/3(id or pk)/
    url(r'^detailprepbook.html/(?P<pk>[0-9]+)/$', views.PrepbookDetailView.as_view(), name = 'detailprepbook'),

    #/buytextbooks/textbooks.html/
    url(r'^textbooks.html/', views.TextbookIndexView.as_view(), name='alltextbooks'),

    #/buytextbooks/prepbooks.html/
    url(r'^prepbooks.html/', views.PrepbookIndexView.as_view(), name='allprepbooks'),

    #/buytextbooks/blog.html/
    url(r'^blog.html/', views.blog, name='blog'),
]
