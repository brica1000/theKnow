from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from bread.models import Orders
from bread.forms import OrderForm

import datetime

# Helper function to tell us todays date
today = datetime.date.today()
days = []
for i in range(6):
    days.append(today + datetime.timedelta(days=i))

# Helper function to count the orders on a particular day and time

#Orders.objects.filter(order_date=tomorrow)


def home(request):
    return render(request, 'bread/home.html', {'days':days})


def order_form(request):
    # post = get_object_or_404(Beliefs)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = OrderForm()
    return render(request, 'bread/order_form.html', {'form': form})
