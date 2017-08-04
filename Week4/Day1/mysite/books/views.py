# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Book


class Home_view(ListView):
    model = Book
    context_object_name = 'books_list'


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
