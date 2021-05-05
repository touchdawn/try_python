from datetime import datetime

from django.http import HttpResponse


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

print(current_datetime(1))