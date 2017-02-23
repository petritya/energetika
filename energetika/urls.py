from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^megrendelesek/$', views.megrendelesek, name='megrendelesek'),
    url(r'^felmeres/$', views.felmeres, name='felmeres'),
    url(r'^nyomtat/$', views.nyomtat, name='nyomtat'),
    url(r'^terulet_sima/$', views.terulet_sima, name='terulet_sima'),
    url(r'^terulet_vagott/$', views.terulet_vagott, name='terulet_vagott'),
    url(r'^tomb/$', views.tomb, name='tomb'),
]