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
    url(r'^privacy-policy/', views.privacy_policy),

    url(r'^2015/08/10/build/a/butcher/block/workbench/', views.serve_article),
    url(r'^2016/03/01/build/a/steel/framed/gate/', views.serve_article),
    url(r'^2016/09/28/Make/a/custom/fumehood/', views.serve_article),
    url(r'^2016/09/30/Mirror/polishing/stainless/steel/', views.serve_article),
    url(r'^2016/10/02/Donald/Trump/and/building/a/wall/', views.serve_article),
    url(r'^2016/10/05/Dos/and/Donts/of/changing/spark/plugs/', views.serve_article),
    url(r'^2016/10/07/Stinson/Beach/and/Google/Photos/', views.serve_article),
    url(r'^2016/10/26/Ingenu/vs/Sigfox/throwdown/', views.serve_article),
    url(r'^2016/11/07/Gate/Progress/', views.serve_article),
    url(r'^2016/11/11/Why/I/voted/for/Gary/Johnson/', views.serve_article),
    url(r'^2016/11/22/Gate/Part/Deux/', views.serve_article)
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
