from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'release_apply/$', 'ticket.views.release_apply'),
    url(r'database_update_apply/$', 'ticket.views.database_update_apply'),
    url(r'database_select_apply/$', 'ticket.views.database_select_apply'),
    url(r'malfunction_apply/$', 'ticket.views.malfunction_apply'),
    url(r'todo_worksheet/$', 'ticket.views.todo_worksheet'),
    url(r'worksheet_detail/$', 'ticket.views.worksheet_detail'),
    url(r'create_detail/$', 'ticket.views.create_detail'),
    url(r'downloadfile/$', 'ticket.views.downloadfile'),
    url(r'create_worksheet/$', 'ticket.views.create_worksheet'),
    url(r'approval_worksheet/$', 'ticket.views.approval_worksheet'),

)
