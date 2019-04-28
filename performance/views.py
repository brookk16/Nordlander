from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs

from django.contrib.auth import get_user_model
from django.db.models import Max
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

from datetime import timedelta, datetime



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
    For bugs_per_week_chart
    Gets a list of the dates of the days in the past week relative to today and formats them to show day/month/year.
    Also counts the amount of bugs added that day, and adds the totals for each day to a list
    """
    seven_days_ago = datetime.now() - timedelta(days=7)
    
    delta = datetime.now() - seven_days_ago
    
    past_week_dates = []
    
    bugs_per_day = []
    

    for i in range(delta.days + 1 ):
        day = (seven_days_ago + timedelta(i))
        day_formatted = day.strftime('%d/%m/%Y')
        past_week_dates.append(day_formatted)
        bugs = (Bugs.objects.filter(created_date=day).count())
        bugs_per_day.append(bugs)
        
    
    """
    For total bugs display
    Shows how many bugs are currently in the database
    """
    bug_count = Bugs.objects.all().count()
    all_bugs = bug_count
    
    
    """
    For bugs_status chart
    Counts all the bugs that have a status of: to do, doing or fixed
    """
    bugs_todo = [Bugs.objects.filter(status="To do").count()] 
    bugs_doing = [Bugs.objects.filter(status="Doing").count()]
    bugs_fixed = [Bugs.objects.filter(status="Fixed").count()]
    
    
     
    
    labels1 = past_week_dates
    labels2 = ["To do", "Doing", "Fixed"]
    data_for_bugs_week = bugs_per_day
    bugs_status = [bugs_todo, bugs_doing, bugs_fixed]
    
   
    
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "data_for_bugs_week": data_for_bugs_week,
        "bugs_status": bugs_status,
        "bugs_todo" : bugs_todo,
        "bugs_doing" : bugs_doing,
        "bugs_fixed" : bugs_fixed,
        }
    
    return JsonResponse(data, safe=False)
