#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r'^select', 'assets.views.Node_select'),
	url(r'^host_list/$', "assets.views.host_list"),
	url(r'^host_add/$', "assets.views.host_add"),
	url(r'^host_add_batch/$', "assets.views.host_add_batch"),
	url(r'^host_detail/$', "assets.views.host_detail", name="host_detail"),
	url(r'^host_edit/$', "assets.views.host_edit", name="host_edit"),
	url(r'^host_edit_batch/$', "assets.views.host_edit_batch"),
	url(r'^host_del/$', "assets.views.host_del", name='host_del'),
	url(r'^host_del_batch/$', "assets.views.host_del_batch"),
	url(r'^host_update/$', "assets.views.host_update"),
	#url(r'^change_info_ajax/$', "assets.views.host_search"),
	url(r'^env/$', 'assets.views.env'),
	url(r'^server_application/$', 'assets.views.server_application'),
	
	url(r'^idc_list/$', "assets.views.idc_list"),
	url(r'^idc_add/$', "assets.views.idc_add"),
	url(r'^idc_edit/$', "assets.views.idc_edit"),
	url(r'^idc_del/$', "assets.views.idc_del"),
	url(r'^idc_type/$', 'assets.views.idc_type_item'),
	
	url(r'^server/type/list/$', "assets.views.server_type_list", name='project_list'),
	url(r'^server/type/add/$', "assets.views.server_type_add"),
	url(r'^server/type/edit/(?P<uuid>[^/]+)/$','assets.views.server_type_edit', name="project_edit_ajax"),
	url(r'^server/type/del/(?P<uuid>[^/]+)/$','assets.views.server_type_del'),
	url(r'^server/server_type/$', 'assets.views.server_type_item'),
	
	
	
	
	
	url(r'^service_add/$', "assets.views.service_add"),
	url(r'service_edit/$', "assets.views.service_edit"),
	url(r'^service_list/$', "assets.views.service_list"),
	url(r'service_del/$', "assets.views.service_del"),
	
)


