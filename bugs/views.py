from django.shortcuts import render, get_object_or_404
from .models import Bugs
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def all_bugs(request):
    """
    Returns all the bugs in the database
    """
    bugs = Bugs.objects.all()
    
    return render(request, "bugs.html", {"bugs": bugs})
    

@login_required
def bug_info(request, pk):
    """
    Returns a single selected feature based on the post ID (pk) and
    render it to the template 'featureInfo.html'.
    Or return a 404 error if the post is not found
    """
    bug = get_object_or_404(Bugs, pk=pk)
    
    
    user = request.user
    
    """current_people_that_liked = feature.user_liked"""
    
    
    return render(request, "bugInfo.html", {'bug': bug}) 

