from django.conf.urls import url, include
from .views import show_performance, graph_data

urlpatterns = [
    url(r'^$', show_performance, name='show_performance'),
    url(r'^api/data', graph_data, name='graph_data'),
]