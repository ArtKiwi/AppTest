# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views
from loginsys.views import login, logout,register

urlpatterns = [
     url (r'^login/$', login),
     url (r'^logout/$', logout),
     url (r'^register/$', register),
     url(r'^password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
     url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
     url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
     url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
