# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book
# from .models import Publisher
# from .models import Author
from .forms import BookForm


def home_view(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def book_list(request):
    myBooks = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': myBooks})


@login_required(login_url='/login/')
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})


def get_bookTitle(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['bookTitle'])
    else:
        form = BookForm()
    return render(request, 'books/book.html', {'form': form})
