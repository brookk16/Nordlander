from django.shortcuts import render, get_object_or_404
from .models import Features

# Create your views here.
def all_features(request):
    """
    Returns all the features in the database
    """
    features = Features.objects.all()
    return render(request, "features.html", {"features": features})

def feature_info(request, pk):
    """
    Returns a single selected feature based on the post ID (pk) and
    render it to the template 'featureInfo.html'.
    Or return a 404 error if the post is not found
    """
    feature = get_object_or_404(Features, pk=pk)
    
    return render(request, "featureInfo.html", {'feature': feature}) 

def like_feature(request, pk):
    
    feature = get_object_or_404(Features, pk=pk)
    
    feature.likes += 1
    feature.save()
    
    return render(request, "featureInfo.html", {'feature': feature}) 