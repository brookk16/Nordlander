from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs
from django.contrib import messages

# Create your views here.
def do_search(request):
    
    search_name = request.GET.get('search', None)
    
    search_type = request.GET.get('search-select-types', None)
    
    search_status = request.GET.get('search-select-status', None)
    
    db_features = request.GET.get('Features', None)
    
    db_bugs = request.GET.get('Bugs', None)
    
  
    
    if request.method == 'GET':
        
        """ 
        Checks that at least one search criteria is input before submission, and sets the correct database to search (features or bugs). If not an error message is displayed and the user is redirected back to viewing all features or bugs.
        """
        
        
        if db_features != None and db_bugs == None:
        
            search_db = Features
    
        elif db_features == None and db_bugs != None: 
        
            search_db = Bugs 
        
            if search_name == "" and search_type == "" and search_status == "":
        
                search_db = search_db.objects.all()
                messages.error(request, "You need to input at least one search criteria!")
            
                if search_db == Features:
                    return render(request, "features.html", {"features": search_db})
            
                elif search_db == Bugs:
                    return render(request, "bugs.html", {"bugs": search_db})
        
        """
        Searches features/bugs db for criteria input in search bar. Users can search using either name, type or status. Or a combination of all three or 2. 
        """
    
        if search_name !="":
            
            if  search_type == "" and search_status =="":
        
                search_db = search_db.objects.filter(name__icontains=request.GET['search'])
        
            elif search_type != "" and search_status =="":
        
                search_db = search_db.objects.filter(name__icontains=request.GET['search'], type=search_type)
                
            elif search_type == "" and search_status !="":
                
                search_db = search_db.objects.filter(name__icontains=request.GET['search'], status=search_status)
        
            elif search_type != "" and search_status !="":
                
                search_db = search_db.objects.filter(name__icontains=request.GET['search'],type=search_type, status=search_status)
                

        elif search_name =="":
            
            if search_type != "" and search_status =="":
                
                search_db = search_db.objects.filter(type=search_type)
            
            elif search_type == "" and search_status !="":
                
                search_db = search_db.objects.filter(status=search_status)
            
            elif search_type != "" and search_status !="":
                
                search_db = search_db.objects.filter(type=search_type, status=search_status)

    """
    Returns users to correct page
    """
    
    if db_features != None and db_bugs == None:
            
        search_db == Features
        return render(request, "features.html", {"features": search_db})
    
    elif db_features == None and db_bugs != None: 
            
        search_db == Bugs
        return render(request, "bugs.html", {"bugs": search_db})
    
    
    
       
        
    

 
    