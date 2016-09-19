from django.conf.urls.defaults import patterns, include, url
from . import views

from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', views.home),
    url(r'^about/', views.about),
    url(r'^contact/', views.contact),
    url(r'^pricing/', views.pricing),
    url(r'^2015/08/10/workBench/', views.home),
    url(r'^2016/03/01/gate/', views.home)
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
