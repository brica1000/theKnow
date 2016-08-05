from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bread_home, name='bread_home'),
    url(r'^order/(?P<order_time>[a-zA-Z]+)$', views.order_form, name='order_form' ),
]
