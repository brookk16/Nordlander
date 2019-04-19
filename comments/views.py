from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comments

# Create your views here.
@login_required
def view_comments(request):
    """
    Returns all the bugs in the database
    """
    comments = Comments.objects.all()
    
    return render(request, "bugs.html", {"comments": comments})
