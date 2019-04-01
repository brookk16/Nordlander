from django.shortcuts import render

# Create your views here.
def homeMessage(request):
    """A view that displays the index page"""
    return render(request, "home.html")
