from django.conf.urls import url, include
from .views import all_features, feature_info, like_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^(?P<pk>\d+)/$', feature_info, name='feature_info'),
    url(r'^(?P<pk>\d+)/$', like_feature, name='like_feature'),
]
