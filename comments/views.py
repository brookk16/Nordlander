from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comments

# Create your views here.
@login_required
def view_comments(request, pk):
    """
    THIS DOESN'T SEEM TO DO ANYTHING
    """
    bug = get_object_or_404(Bugs, pk=pk)
    
    """comments = Comments.objects.all()"""
    
    
    
   
        
    
    comments = Comments.objects.all()
    
    
    
   
    
    return render(request, "bugInfo.html", {'bug': bug}, {'comments': comments})
    
   
