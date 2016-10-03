from django.conf.urls import url
from . import views

from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^$', views.home),
    url(r'^about/', views.about),
    url(r'^store/', views.store),


    url(r'^2015/08/10/build/a/butcher/block/workbench/', views.serve_article),
    url(r'^2016/03/01/build/a/steel/framed/gate/', views.serve_article),
    url(r'^2016/09/28/Make/a/custom/fumehood/', views.serve_article),
    url(r'^2016/09/30/Mirror/polishing/stainless/steel/', views.serve_article),
    url(r'^2016/10/02/Donald/Trump/and/building/a/wall/', views.serve_article) 

    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
