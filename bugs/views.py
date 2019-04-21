from django.shortcuts import render, get_object_or_404
from .models import Bugs
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from comments.models import Comments





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
    Returns a single selected bug based on the bug ID (pk) and
    render it to the template 'bugInfo.html'.
    Or return a 404 error if the post is not found
    
    Also returns all the comments for that bug
    
    And the form for adding new comments
    """
    bug = get_object_or_404(Bugs, pk=pk)
    
    comments = Comments.objects.filter(bug_id=pk).order_by("-created_date")
    
    current_upvote = bug.user_upvoted
    user = request.user
    
    
    
    
    if request.GET.get('upvote') == 'upvote':
        
        if user not in current_upvote.all():
        
            bug.upvotes += 1
            current_upvote.add(user)
            bug.save()
        
        else:
            messages.success(request, 'You have already upvoted this')
            
    
    return render(request, "bugInfo.html", {'comments': comments, 'bug': bug}) 

