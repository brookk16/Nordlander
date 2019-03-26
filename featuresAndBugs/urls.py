from django.conf.urls import url, include
from .views import all_features_and_bugs

urlpatterns = [
    url(r'^$', all_features_and_bugs, name='featuresAndBugs'),
]
