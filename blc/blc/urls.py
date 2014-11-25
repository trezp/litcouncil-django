from django.conf.urls import patterns, include, url
from django.contrib import admin
from beav_lit_council import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^board_info', views.board_info, name='board_info'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^locations', views.locations, name='locations'),
	url(r'^tutorinfo', views.tutorinfo, name='tutorinfo'),
	url(r'^volunteer', views.volunteer, name='volunteer'),
	url(r'^calendars', views.calendars, name='calendars'),
	url(r'^schedules', views.schedules, name='schedules'),
	url(r'^links', views.links, name='links'),
	url(r'^volunteers', views.volunteer, name='volunteer'),
    url(r'^admin/', include(admin.site.urls)),)
