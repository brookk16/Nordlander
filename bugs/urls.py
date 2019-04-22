from django.conf.urls import url, include
from .views import all_bugs, bug_info, add_bug



urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_info, name='bug_info'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
]