from django.conf.urls import patterns, url

from basics import views

urlpatterns = patterns('',
    # ex: /basics/
    url(r'^$', views.index, name='index'),
)

