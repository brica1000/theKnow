from blog.forms import SearchOrgForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


# This seems to make it work, but we still display the last entry
def search_form(request):
    if request.method == "POST":
        search_form = SearchOrgForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    else:
        search_form = SearchOrgForm()
    return {'search_form' : search_form}
