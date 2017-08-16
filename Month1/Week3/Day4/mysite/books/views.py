# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import NameForm
from .models import Book
# from .models import Author
# from .models import Publisher


def book_list(request):
    myBooks = Book.objects.all()
    return render(request, 'book_list.html', {'books': myBooks})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'detail.html', {'book': book})


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'books/search-results.html',
                      {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
    return HttpResponse(message)


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
