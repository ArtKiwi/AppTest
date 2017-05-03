# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, context, Template
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib import auth
from loginsys.forms import RegistrationForm
# Create your views here.

#def login(request):
#    args = {}
#    args.update(csrf(request))
#    if request.POST:
#        username = request.POST.get('username','')
#        password = request.POST.get('password', '')
#        user = auth.authenticate(username=username, password=password)
#        if user is not None:
#            auth.login(request, user)
#            return redirect ('/')
#        else:
#            args ['login_error'] = "user not found"
#            return  render(request,'login.html', args)
#    else:
#        return  render(request,'login.html', args)

def logout (request):
    auth.logout(request)
    return redirect ('/')

def register (request):
    args={}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['from']=newuser_form
    return render(request,'register.html', args)

