# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book
from .forms import BookForm


class Home_view(View):
    books = Book.objects.all()

    def get(self, request):
        return render(request, 'books/index.html', {'books': self.books})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Book_list(ListView):
    model = Book
    context_object_name = 'books_list'


# @login_required(login_url='/login/')
class Book_detail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(Book_detail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


def get_BookForm(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    return render(request, 'books/book.html', {'form': form})


def login_form(request):
    return render(request, 'books/login_form.html')


# @login_required()
def login_result(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # return HttpResponse('You are logged in successfully')
        myBooks = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': myBooks})
    else:
        return HttpResponse('Invalid Login')
