from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Comments
from bugs.models import Bugs





# Create your views here.

@login_required
def add_comment(request, pk):
    
    bug = get_object_or_404(Bugs, pk=pk)
    
    comments = Comments.objects.filter(bug_id=pk).order_by("-created_date")
    
    user = request.user.username
    
    
    
    """
    Creates a new comment for the bug. 'Username' field is not used for the app, but is needed to view in admin panel.
    """
    
    if request.method == "POST":
        
        new_comment = Comments.objects.create(
            username = user,
            user_id = request.user,
            bug_id = bug,
            comment = request.POST.get('new-comment', None)
            )
        
        new_comment.save()
        
        
    return render(request, 'bugInfo.html', {'bug': bug, 'comments': comments})
    

def like_comment(request, pk):
     
    comment = get_object_or_404(Comments, pk=pk)
    current_liked = comment.user_id
    user = request.user
    
   
    
    
    
    
   
    if request.GET.get('like') == 'like':
        
        if user not in current_liked.all():
        
            comment.upvotes += 1
            current_liked.add(user)
            comment.save()
        
        else:
            messages.success(request, 'You have already liked this')
    
    return render(request, "home.html") 
   
