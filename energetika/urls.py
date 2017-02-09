from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^megrendelesek/$', views.megrendelesek, name='megrendelesek'),
    url(r'^megrendelesek/(?P<pk>[0-9]+)/$', views.megrendelesek, name='megrendelesek'),
]