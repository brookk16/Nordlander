from django.shortcuts import render

# Create your views here.
def show_performance(request):
    """A view that displays the index page"""
    return render(request, "performance.html")
