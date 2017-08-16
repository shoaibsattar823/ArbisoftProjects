from django.http import HttpResponse
from django.http import Http404
# from django.template.loader import get_template
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello WORLD")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('mytemplate.html')
    return render(request, 'mytemplate.html', {'current_date': now})
    # return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = ('<html><body>In {of} hour(s)'
            ', it will be  {dt}.</body></html>'
            ).format(of=offset, dt=dt)
    return HttpResponse(html)
