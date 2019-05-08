from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Bugs
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bugs.forms import AddBugForm
from comments.models import Comments

# Create your views here.

@login_required
def all_bugs(request):
    """
    Returns all the bugs in the database by created date. Also adds the form for adding bug comments.
    """
    bugs = Bugs.objects.all().order_by("-created_date")
    
    add_bug_form = AddBugForm()
    
    return render(request, "bugs.html", {"bugs": bugs, "add_bug_form": add_bug_form})
    

@login_required
def bug_info(request, pk):
    """
    Returns a single selected bug based on the bug ID (pk) and
    render it to the template 'bugInfo.html'.
    Or return a 404 error if the post is not found
    
    Also returns all the comments for that bug
    
    Also lets users upvote bugs, if they haven't already liked it.
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


def add_bug(request): 
    """
    Allows user to add a bug comment.
    """
    
    if request.method == 'POST':
        
        user_form = AddBugForm(request.POST)
        
        if user_form.is_valid():
            
            user_form.save()
            
        else:
            
            user_form = AddBugForm()
    
    return redirect(reverse('bugs'))
    
