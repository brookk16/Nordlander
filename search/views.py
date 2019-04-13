from django.shortcuts import render
from features.models import Features

# Create your views here.
def do_search(request):
    
    if request.method == 'GET':
    
        if request.GET.get('search', None) !="" and request.GET.get('search-select', None) == "":
        
            features = Features.objects.filter(name__icontains=request.GET['search'])
        
    
        elif request.GET.get('search', None) !="" and request.GET.get('search-select', None) != "":
        
            features = Features.objects.filter(name__icontains=request.GET['search'], type=request.GET.get('search-select', None))
        
        elif request.GET.get('search', None) =="" and request.GET.get('search-select', None) != "":
            
            features = Features.objects.filter(type=request.GET.get('search-select', None))

    
    
    return render(request, "features.html", {"features": features})
    
