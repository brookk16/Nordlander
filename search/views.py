from django.shortcuts import render
from features.models import Features

# Create your views here.
def do_search(request):
    features = Features.objects.filter(name__icontains=request.GET['search'])
    return render(request, "features.html", {"features": features})
    
    
