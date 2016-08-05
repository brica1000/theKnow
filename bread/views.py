from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from bread.models import Orders
from bread.forms import OrderForm

import datetime
"""
Helpers
"""
# Helper function to count the orders on a particular day and time
def remaining_orders(days):
    morning = []
    evening = []
    for day in days:
        orders_then = len(Orders.objects.filter(order_date=day, order_slot="morning"))
        orders_later = len(Orders.objects.filter(order_date=day, order_slot="afternoon"))
        if orders_then <= 6:
            morning.append(6 - orders_then)
        else:
            morning.append(0)
        if orders_later <=6:
            evening.append(6 - orders_later)
        else:
            evening.append(0)
    return morning, evening


"""
The views
"""
def bread_home(request):
    today = datetime.date.today()
    days = []
    for i in range(7):
        days.append(today + datetime.timedelta(days=i))

    # Combine the data
    (morning, evening) = remaining_orders(days)
    zipped = zip(morning, evening, days)
    return render(request, 'bread/home.html', {'zipped':zipped,})


def order_form(request, order_time):
    # post = get_object_or_404(Beliefs)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('bread_home'))
    else:
        form = OrderForm()
    return render(request, 'bread/order_form.html', {'form': form,})
