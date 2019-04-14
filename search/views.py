from django.shortcuts import render
from features.models import Features

# Create your views here.
def do_search(request):
    
    search_name = request.GET.get('search', None)
    
    search_type = request.GET.get('search-select-types', None)
    
    search_status = request.GET.get('search-select-status', None)
    
    db_features = request.GET.get('Features', None)
    
    db_bugs = request.GET.get('bugs', None)
    
    if db_features != None and db_bugs == None:
        
        search_db = Features
    
    elif db_features == None and db_bugs != None: 
        
        search_db = Bugs
    
    
    
    if request.method == 'GET':
        
        
        if search_name !="":
            
            if  search_type == "" and search_status =="":
        
                features = search_db.objects.filter(name__icontains=request.GET['search'])
        
            elif search_type != "" and search_status =="":
        
                features = search_db.objects.filter(name__icontains=request.GET['search'], type=search_type)
                
            elif search_type == "" and search_status !="":
                
                features = search_db.objects.filter(name__icontains=request.GET['search'], status=search_status)
        
            elif search_type != "" and search_status !="":
                
                features = search_db.objects.filter(name__icontains=request.GET['search'],type=search_type, status=search_status)
                

        elif search_name =="":
            
            if search_type != "" and search_status =="":
                
                features = search_db.objects.filter(type=search_type)
            
            elif search_type == "" and search_status !="":
                
                features = search_db.objects.filter(status=search_status)
            
            elif search_type != "" and search_status !="":
                
                features = search_db.objects.filter(type=search_type, status=search_status)


    return render(request, "features.html", {"features": features})
    
    request.GET.get('search-select-status', None)
    