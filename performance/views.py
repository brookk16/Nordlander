from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs

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
