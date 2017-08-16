# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from home_services.forms import RegisterForm
from home_services.models import Service


# Create your views here.
class HomePage(ListView):
    model = Service
    context_object_name = 'services'


class RegisterCustomer(FormView):
    template_name = 'home_services/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password1'],
                                 email=form.cleaned_data['email'])
        return super(RegisterCustomer, self).form_valid(form)


class RequestService(CreateView):
    model = Service
    fields = ['category']


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
