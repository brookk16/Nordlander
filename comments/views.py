from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Comments
from bugs.models import Bugs

from django.contrib.auth import get_user_model



# Create your views here.

@login_required
def add_comment(request, pk):
    
    bug = get_object_or_404(Bugs, pk=pk)
    
    comments = Comments.objects.filter(bug_id=pk)
    
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

        
   
"""
form = CommentsForm(request.POST)
        
        
        
        if form.is_valid():
            
            comment = form.cleaned_data['comment']
            
            form.save(commit=False)
            
            username = request.user
            user_id = request.user.id
            bug_id = pk
            
            form.save()
"""