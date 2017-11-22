#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^login/$', "account.views.user_login"),
	url(r'^loginout/$', "account.views.logout_view"),
	url(r'registration/$', 'account.views.user_registration'),
    url(r'basic_info/$', 'account.views.basic_info'),
    url(r'create_user/$', 'account.views.create_user'),
    url(r'del_user/$', 'account.views.del_user'),
    url(r'create_group/$', 'account.views.create_group'),
    url(r'del_group/$', 'account.views.del_group'),
    url(r'group_permission_modif/$', 'account.views.group_permission_modif'),
    url(r'permission_info/$', 'account.views.permission_info'),
    url(r'user_to_group/$', 'account.views.user_to_group'),
    url(r'groupdeluser/$', 'account.views.group_del_user'),
)


