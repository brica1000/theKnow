from bread.models import Orders
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime


# This works, but we need Day objects..
def days(request):
    # maybe this isn't efficient?
    days = []
    for i in range(6):
        days.append(datetime.datetime.now() + datetime.timedelta(days=i))


    return {'days':days}
