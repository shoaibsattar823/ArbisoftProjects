from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

import datetime

from books.models import Book


def hello(request):
    return HttpResponse("Hello WORLD")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_time.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'offset': offset,
                                                'dt': dt,
                                                })


def book_list(request):
    mybooks = Book.objects.all()
    return render(request, 'book_list.html', {'mybooks': mybooks})
