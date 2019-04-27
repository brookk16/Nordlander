from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs

from django.contrib.auth import get_user_model
from django.db.models import Max
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

# Create your views here.
def show_performance(request):
    
    """
    Returns top 5 features based on likes
    """
    top_scores_features = Features.objects.order_by('-likes').values_list('likes', flat=True).distinct()
    top_features = Features.objects.order_by('-likes').filter(likes__in=top_scores_features)[:5]
    
    """
    Returns top 5 bugs based on upvotes
    """
    top_scores_bugs = Bugs.objects.order_by('-upvotes').values_list('upvotes', flat=True).distinct()
    top_bugs = Bugs.objects.order_by('-upvotes').filter(upvotes__in=top_scores_bugs)[:5]
    
    
    
    
    
    
    return render(request, "performance.html", {'top_features': top_features, 'top_bugs': top_bugs})


def graph_data(request):
    
    User = get_user_model()
    
    user_count = User.objects.all().count()
    bug_count = Bugs.objects.all().count()
    feature_count = Features.objects.all().count()
    bug_max = Bugs.objects.all().aggregate(Max('upvotes'))
    feature_max = Features.objects.all().aggregate(Max('likes'))
    
    bugs_and_features_todo = (Bugs.objects.filter(status="To do").count()) + (Features.objects.filter(status="To do").count())
    bugs_and_features_doing = (Bugs.objects.filter(status="Doing").count()) + (Features.objects.filter(status="Doing").count())
    bugs_and_features_done = (Bugs.objects.filter(status="Fixed").count()) + (Features.objects.filter(status="Available").count())
    
    
     
    features_max_upvote = feature_max
    labels1 = ["Users", "Bugs", "Features"]
    labels2 = ["Bugs", "Features"]
    labels3 = ["To do", "Doing", "Done"]
    default = [user_count, bug_count, feature_count]
    max_values = [bug_max["upvotes__max"], feature_max["likes__max"]]
    bugs_and_feature_status = [bugs_and_features_todo, bugs_and_features_doing, bugs_and_features_done]
    
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "labels3": labels3,
        "default": default,
        "max_values": max_values,
        "bugs_and_feature_status": bugs_and_feature_status
    }
    return JsonResponse(data, safe=False)
