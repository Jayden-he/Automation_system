from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmdb_v4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'account/', include("account.urls")),
	url(r'^$', 'account.views.basic_info'),
	url(r'assets/', include("assets.urls")),
	url(r'ticket', include('ticket.urls')),
)
