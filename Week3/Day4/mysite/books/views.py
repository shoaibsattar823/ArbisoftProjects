# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Book
# from .models import Author
# from .models import Publisher


def book_list(request):
    myBooks = Book.objects.all()
    return render(request, 'book_list.html', {'books': myBooks})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'detail.html', {'book': book})
