from django.conf.urls import include, url
from article import views

urlpatterns = [
     url(r'^articles/all/$', views.articles),
     url(r'^addarticle/$', views.addarticle),
     url(r'^edit/(?P<id>\d+)/$', views.editarticle),
     url(r'^articles/get/(?P<article_id>\d+)/$', views.article),
     url(r'^page/(\d+)/articles/addlike/(?P<article_id>\d+)/$', views.addlike),
     url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike),
     url(r'^article/addcomment/(?P<article_id>\d+)/', views.addcomment),
     url(r'^page/(\d+)/$', views.articles),
     url(r'^$', views.articles),
]
