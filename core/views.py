import datetime

from django.http import HttpResponse


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> Welcome,It is now %s.</body></html>" % now
    return HttpResponse(html)
