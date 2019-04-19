from django.shortcuts import render, get_object_or_404
from .models import Bugs
from django.contrib.auth.decorators import login_required

from comments.models import Comments
from django.db.models import Q

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
    
    comments = Comments.objects.all()
    
   
        
    
    """comments = Comments.objects.get(bug_id=pk).order_by('created_date').first()"""
    
   
    
    return render(request, "bugInfo.html", {'bug': bug}, {'comments': comments}) 

