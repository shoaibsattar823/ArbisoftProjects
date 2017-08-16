# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from books.forms import RegisterForm
from django.contrib.auth.models import User

from .models import Book


class Home_view(ListView):
    model = Book
    context_object_name = 'books_list'


class RegisterUser(FormView):
    template_name = 'books/register_user.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password1'],
                                 email=form.cleaned_data['email']
                                 )
        return super(RegisterUser, self).form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Book_list(ListView):
    model = Book
    context_object_name = 'books_list'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Book_detail(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'book_detail'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class BookAdd(CreateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date']
