# The URL MAPPER provides the mapping between URL's and Views
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
urlpatterns = [

            url(r'^login/$',auth_views.login, {'template_name': 'login.html'}, name='login'),
            url(r'^logout/$',auth_views.logout, {'next_page': '/login/'}),
            url(r'^account/$', views.avail_list, name='avail_list'),
            url(r'^account/create$', views.avail_create, name='avail_create'),
            url(r'^account/(?P<id>\d+)/update$', views.avail_update, name='avail_update'),
            url(r'^account/(?P<id>\d+)/delete$',views.avail_delete, name='avail_delete'),
           

            ]

