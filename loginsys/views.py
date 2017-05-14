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
from django.contrib.auth.forms import UserChangeForm


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm(instance=user)
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
            args['form'] = newuser_form
    return render(request, 'register.html', args)


@login_required
def profile(request):
    return render(request, 'profile.html')


# need help
@login_required
def edituserinfo(request):
    user = request.user
    form = UserChangeForm(instance=user)
    if request.POST:
        change_form = UserChangeForm(request.POST, instance=user)
        if change_form.is_valid():
            user = change_form.save(commit=False)
            user.save()
            return redirect('/auth/profile/')
        else:
            form = change_form
    return render(request, 'editinfo.html', {'form': form})
