# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, context, Template
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib import auth
from loginsys.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'],
                password=newuser_form.cleaned_data['password2']
            )
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['from'] = newuser_form
    return render(request, 'register.html', args)


@login_required
def profile(request):
    return render(request, 'profile.html')
