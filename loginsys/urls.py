# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views
from loginsys.views import register, profile
from loginsys.forms import MyAuthenticationForm


urlpatterns = [
     url(r'^register/$', register),
     url(r'^profile/$', profile),
     url(r'^login/$', views.LoginView.as_view(template_name='login.html',
        authentication_form=MyAuthenticationForm), name='login'),
     url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
     url(r'^password_change/$', views.PasswordChangeView.as_view(
        template_name='password_change.html'), name='password_change'),
     url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(
        template_name='mypassword_change_done.html'), name='password_change_done'),
     url(r'^password_reset/$', views.PasswordResetView.as_view(
        template_name='mypassword_reset_form.html'), name='password_reset'),
     url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(
        template_name='mypassword_reset_done.html'), name='password_reset_done'),
     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.PasswordResetConfirmView.as_view(template_name='mypassword_reset_confirm.html'
         ), name='password_reset_confirm'),
     url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(
        template_name='mypassword_reset_complete.html'), name='password_reset_complete'),
]
