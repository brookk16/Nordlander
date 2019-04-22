from django.shortcuts import render
from features.models import Features

# Create your views here.
def show_performance(request):
    """A view that displays the index page"""
    
    """
    NEED TO TEST: should return top 5 features based on likes
    """
    top_scores = (Features.objects
                     .order_by('-likes')
                     .values_list('likes', flat=True)
                     .distinct())
    top_records = (myModel.objects
                      .order_by('-likes')
                      .filter(score__in=top_scores[:5]))
    
    
    print(top_records)
    
    
    
    return render(request, "performance.html")
