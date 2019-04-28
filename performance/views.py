from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs

from django.contrib.auth import get_user_model
from django.db.models import Max
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

from datetime import datetime, timedelta


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
    
    
    
    """
    Gets a list of the dates of the days in the past week and month (month as an average of 30 days) and formats them to show day/month/year
    """
    seven_days_ago = datetime.today() - timedelta(days=7)
    
    month_ago = datetime.today() - timedelta(days=30)
    
    delta = datetime.today() - seven_days_ago
    delta2 = datetime.today() - month_ago
    
    past_week_dates = []
    past_months_dates = []

    for i in range(delta.days + 1):
        day = (seven_days_ago + timedelta(i)).strftime('%d/%m/%y')
        past_week_dates.append(day)
    
    for i in range(delta2.days + 1):
        day = (month_ago + timedelta(i)).strftime('%d/%m/%y')
        past_months_dates.append(day)
        
    
      
   
    
    
    
    
    
    #User = get_user_model()
    
    #user_count = User.objects.all().count()
    bug_count = Bugs.objects.all().count()
    feature_count = Features.objects.all().count()
    bug_max = Bugs.objects.all().aggregate(Max('upvotes'))
    feature_max = Features.objects.all().aggregate(Max('likes'))
    
    bugs_todo = (Bugs.objects.filter(status="To do").count()) 
    bugs_doing = (Bugs.objects.filter(status="Doing").count()) 
    bugs_fixed = (Bugs.objects.filter(status="Fixed").count())
    
    
     
    features_max_upvote = feature_max
    labels1 = [past_week_dates]
    labels2 = [past_months_dates]
    labels3 = ["To do", "Doing", "Fixed"]
    default = [bug_count, feature_count]
    max_values = [bug_max["upvotes__max"], feature_max["likes__max"]]
    bugs_status = [bugs_todo, bugs_doing, bugs_fixed]
    
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "labels3": labels3,
        "default": default,
        "max_values": max_values,
        "bugs_status": bugs_status
    }
    return JsonResponse(data, safe=False)
