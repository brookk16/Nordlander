from django.conf.urls import url
from .views import view_comments

urlpatterns = [
    url(r'^$', view_comments, name='view_comments')
]
