# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Book
# from .models import Publisher
# from .models import Author


# Create your views here.
def login_form(request):
    # print '*****Reached over here*****'
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
    return HttpResponse('You are now logout from the website.')


def book_list(request):
    # if not request.user.is_authenticated:
    #    return render(request, 'books/login_error.html')
    myBooks = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': myBooks})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})
