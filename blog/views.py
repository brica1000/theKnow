from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .forms import CSInputForm, PostForm, OrgForm, NewsForm, SearchOrgForm
from .models import Beliefs, Vari, Org, NewsFeed, Search

from modules.mymodule import Shape
from modules.mymodule import Searches





def blog_home(request):
    news_events = NewsFeed.objects.order_by('-published_date')
    return render(request, 'blog/home.html', {'news_events': news_events,})


def add_news_event(request):
    news_event = NewsFeed()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news_event)
        if form.is_valid(): # form is not saving! Why?
            news_event = form.save(commit=False)
            news_event.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = NewsForm(instance=news_event)
    return render(request, 'blog/add_news_event.html', {'form': form})




def modify_news_event(request, pk):
    news_event = get_object_or_404(NewsFeed, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news_event)
        if form.is_valid():
            news_event = form.save(commit=False)
            news_event.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = NewsForm(instance=news_event)
    return render(request, 'blog/modify_news_event.html', {'form':form})


def my_beliefs(request):
    post = Beliefs.objects.all()[0]
    return render(request, 'blog/my_beliefs.html', {'post': post})


def edit_beliefs(request, pk):
    post = get_object_or_404(Beliefs, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('my_beliefs'))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_beliefs.html', {'form': form})


def organizations(request):
    organizations = Org.objects.all()
    if request.method == "POST":
        search_form = SearchOrgForm(request.POST)
        if search_form.is_valid():
            search_form.save()
            return HttpResponseRedirect(reverse('search_results'))
    else:
        search_form = SearchOrgForm()
    return render(request, 'blog/organizations.html', {'organizations': organizations,'search_form':search_form})


def modify(request, pk):
    organization = get_object_or_404(Org, pk=pk)
    if request.method == "POST":
        form = OrgForm(request.POST, instance=organization)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.save()
            return HttpResponseRedirect(reverse('organizations'))
    else:
        form = OrgForm(instance=organization)
    return render(request, 'blog/modify.html', {'form': form})


def contribute(request):
    post = Beliefs.objects.all()[1]
    return render(request, 'blog/contribute.html', {'post':post})

"""
Searches - refactor the searchs into modules!
"""
def search_results(request):
    stuff = Search.objects.all()[len(Search.objects.all())-1].search_input # We can do better, but for now....lets be naive.
    organizations = Org.objects.all()
    results = Searches.search_basic(stuff, organizations)
    return render(request, 'blog/search_results.html', {'results':results})



def global_search(request): # for now, let it be the same
    # This is taking the last search from above!!
    stuff = Search.objects.all()[len(Search.objects.all())-1].search_input # We can do better, but for now....lets be naive.
    organizations = Org.objects.all()
    results = []
    for organization in organizations:
        if stuff in organization.all_data().lower():
            results.append(organization)
    return render(request, 'blog/global_search.html', {'results':results})


def directory(request):
    links = NewsFeed.objects.all()
    beliefs = Beliefs.objects.all()[0]
    contribuy = Beliefs.objects.all()[1]
    organizations = Org.objects.all()
    return render(request, 'blog/directory.html', {'links':links, 'beliefs':beliefs, 'organizations':organizations,'contribuy':contribuy})

"""
"""


def cs_scrape(request):
    if request.method == "POST":
        form = CSInputForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            return HttpResponseRedirect(reverse('cs_results'))
    else:
        form = CSInputForm()
    return render(request, 'blog/cs_scrape.html', {'form': form})

def cs_results(request):
    results = Vari.objects.all()
    x = int(results[len(results)-1].value) # Input(a number) to operate on
    t = results[len(results)-1].type1
    output = Shape.NuttyNumber(x, t)
    return render(request, 'blog/cs_results.html', {'results': results, 'output': output})


def clothing_design(request):
    return render(request, 'blog/clothing_design.html')


def secret(request):
    return render(request, 'blog/secret.html')
