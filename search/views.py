from django.shortcuts import render
from features.models import Features
from django.contrib import messages

# Create your views here.
def do_search(request):
    
    search_name = request.GET.get('search', None)
    
    search_type = request.GET.get('search-select-types', None)
    
    search_status = request.GET.get('search-select-status', None)
    
    db_features = request.GET.get('Features', None)
    
    db_bugs = request.GET.get('Bugs', None)
    
    """ 
    Checks that at least one search criteria is input before submission, and sets the correct database to search (features or bugs). If not an error message is displayed and the user is redirected back to viewing all features or bugs.
    """
    
    if search_name == "" and search_type == "" and search_status == "":
        
        features = Features.objects.all()
        messages.error(request, "You need to input at least one search criteria!")
        render(request, "features.html", {"features": features})
        
    
    else:
        
        if db_features != None and db_bugs == None:
        
            search_db = Features
    
        elif db_features == None and db_bugs != None: 
        
            search_db = Bugs
    
    
    
    """
    Searches features/bugs db for criteria input in search bar. Users can search using either name, type or status. Or a combination of all three or 2. 
    """
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
    
 
    