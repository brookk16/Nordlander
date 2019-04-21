from django.shortcuts import render, get_object_or_404
from .models import Features
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def all_features(request):
    """
    Returns all the features in the database
    """
    features = Features.objects.all()
    return render(request, "features.html", {"features": features})


@login_required
def feature_info(request, pk):
    """
    Returns a single selected feature based on the post ID (pk) and
    render it to the template 'featureInfo.html'.
    Or return a 404 error if the post is not found
    """
    feature = get_object_or_404(Features, pk=pk)
    
   
    
    current_liked = feature.user_liked
    user = request.user

    if request.GET.get('like') == 'like':
        
        if user not in current_liked.all():
        
            feature.likes += 1
            current_liked.add(user)
            feature.save()
        
        else:
            messages.success(request, 'You have already liked this')
            
    
    return render(request, "featureInfo.html", {'feature': feature}) 

