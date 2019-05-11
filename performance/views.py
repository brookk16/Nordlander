from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs
from django.contrib.auth import get_user_model
from django.db.models import Max
from django.db import connections
from django.db.models import Count, Sum, F
from django.http import JsonResponse
from datetime import timedelta, datetime
from django.utils import timezone

User = get_user_model()

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
    seven_days_ago = datetime.today() - timedelta(days=6)
    
    delta = datetime.today() - seven_days_ago
    
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
    
    """
    For current_feature_types chart
    Gets a list of all curently used feature types (which come as objects, thus the values need to be extracted), and counts how many features beong to each type.
    """
    currently_used_feature_types_objects = Features.objects.order_by('type').values('type').distinct()
    
    currently_used_feature_types = []
   
    
    amount_of_features_per_types = []
    
    for feature_type in currently_used_feature_types_objects:
        currently_used_feature_types.append(feature_type['type'])
    
    i = 0
    
    while i < len(currently_used_feature_types):
        feature = (Features.objects.filter(type=currently_used_feature_types[i])).count()
        amount_of_features_per_types.append(feature)
        i += 1
    
    """
    For bugs_per_feature chart
    Gathers all the different bug types, and then counts how many of the total bugs belong in to each type
    """
    bugs_by_type = Bugs.objects.order_by('type').values('type').distinct()
    
    currently_used_bug_types = []
    amount_of_bugs_per_feature_type = []
    
    for bug_type in bugs_by_type:
        currently_used_bug_types.append(bug_type['type'])
   
    amount_of_bugs_per_feature_type_dict = Bugs.objects.annotate(type_of=F('type')).values('type').annotate(bug_count=Count('id'))
    
    
    l = 0
    
    while l < len(amount_of_bugs_per_feature_type_dict):
        bug_count = amount_of_bugs_per_feature_type_dict[l]['bug_count']
        amount_of_bugs_per_feature_type.append(bug_count)
        l += 1
        
        
    """
    Counts the amount of user likes per feature type(shows which types are more popular with users).The number of likes are then extracted from thes dict and passed into a list.
    """
    
    likes_per_feature_type_dict = Features.objects.values('type').annotate(total_likes=Sum('likes')).order_by('type')
    likes_per_feature_type = []
    
    k = 0
    
    while k < len(likes_per_feature_type_dict):
        likes_count = likes_per_feature_type_dict[k]['total_likes']
        likes_per_feature_type.append(likes_count)
        k += 1
    
    
    """
    For new_users_chart
    Counts all users who joined in the past week and counts them. The second variable stores the number of users who joined before last week
    """
    users_joined_in_last_week = User.objects.filter(date_joined__gte=timezone.now()-timedelta(days=7)).count()
    
    users_joined_older_last_week = User.objects.all().count() - users_joined_in_last_week
     
     
    labels1 = past_week_dates
    labels2 = ["To do", "Doing", "Fixed"]
    labels3 = currently_used_feature_types
    labels4 = currently_used_bug_types
    labels5 = ["New Users", "Existing Users"]
    labels6 = currently_used_feature_types
    data_for_bugs_week = bugs_per_day
    bugs_status = [bugs_todo, bugs_doing, bugs_fixed]
    new_users_data = [users_joined_in_last_week, users_joined_older_last_week]
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "labels3": labels3,
        "labels4": labels4,
        "labels5": labels5,
        "labels6": labels6,
        "data_for_bugs_week": data_for_bugs_week,
        "bugs_status": bugs_status,
        "amount_of_features_per_types": amount_of_features_per_types,
        "amount_of_bugs_per_feature_type": amount_of_bugs_per_feature_type,
        "likes_per_feature_type": likes_per_feature_type,
        "new_users_data": new_users_data,
        }
    
    return JsonResponse(data, safe=False)
