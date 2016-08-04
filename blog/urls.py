from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^home/', views.blog_home, name='home'),
    url(r'^(?P<pk>\d+)/modify_news_event/$', views.modify_news_event, name='modify_news_event'),
    url(r'^add_news_event/', views.add_news_event, name='add_news_event'),
    url(r'^my_beliefs/', views.my_beliefs, name='my_beliefs'),
    url(r'^update/(?P<pk>\d+)/$', views.edit_beliefs, name='edit_beliefs'),
    url(r'^cs_scrape/', views.cs_scrape, name='cs_scrape'),
    url(r'^cs_results/', views.cs_results, name='cs_results'),
    url(r'^clothing_design/', views.clothing_design, name='clothing_design'),
    url(r'^organizations/', views.organizations, name='organizations'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^global_search/', views.global_search, name='global_search'),
    url(r'^directory/', views.directory, name='directory'),
    # Beware, this won't render the right page!!! Why?
    # url(r'^organizations/(?P<pk>\d+)/modify/$', views.modify, name='modify'),
    url(r'^modify/(?P<pk>\d+)/$', views.modify, name='modify'),
    url(r'^contribute/', views.contribute, name='contribute'),
    url(r'^secret/', views.secret, name='secret'),
]
