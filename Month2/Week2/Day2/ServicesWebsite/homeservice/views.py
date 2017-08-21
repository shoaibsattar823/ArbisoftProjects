# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse

from homeservice.forms import RegisterForm, RequestForm
from homeservice.models import Service, Order, Customer


# Create your views here.
class HomePage(ListView):
    model = Service
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        requests = Order.objects.filter(ordered_by=str(self.request.user))
        requests = [r.ordered_service for r in requests]
        # print requests
        context.update({
            # 'customer': Customer.objects.get(username=self.request.user),
            'requests': requests,
        })
        return context


class NewRequest(TemplateView):
    template_name = 'homeservice/newrequest.html'

    def get(self, request):
        # print('here')
        form = RequestForm()
        # print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            print('reached inside')
            # print request.user
            c = Customer.objects.get(username=request.user)
            # print form.cleaned_data['service_type']
            st = form.cleaned_data['service_type']
            s = Service.objects.get(service_type=st)
            Order.objects.create(ordered_by=c, ordered_service=s,
                                 ordered_date=datetime.date.today())
            # service_type = form.cleaned_data['service_type']

        # args = {'form': form, 'service_type': service_type}
        return HttpResponseRedirect('/')
        # return render(request, 'homeservice/index.html',
        #              {'ans': form.cleaned_data['service_type']})


class RequestDetail(View):
    def get(self, request):
        requests = Order.objects.filter(ordered_by=str(self.request.user))
        requests = [[r.ordered_service, r.ordered_date, r.status]
                    for r in requests]
        return render(request, 'homeservice/request_detail.html',
                      {'requests': requests})


class JsonDetail(View):
    def get(self, request):
        requests = Order.objects.filter(ordered_by=str(self.request.user))
        requests = [[r.ordered_service, r.ordered_date, r.status]
                    for r in requests]
        req_json_format = []
        for r in requests:
            req_json_format.append({
                            'Service': str(r[0]),
                            'Date': str(r[1]),
                            'Status': r[2]
                            })
        """
        I have created a list of dict of the orders of a specific customer in
        above loop then converted it
        to json format in the below line
        """
        req_json_format = json.dumps(req_json_format)
        return HttpResponse(req_json_format)


class RegisterUser(FormView):
    template_name = 'homeservice/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password1'],
                                 email=form.cleaned_data['email'])
        return super(RegisterUser, self).form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
