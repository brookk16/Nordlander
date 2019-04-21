from django.conf.urls import url
from .views import add_comment, like_comment

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/$', like_comment, name='like_comment'),
]
