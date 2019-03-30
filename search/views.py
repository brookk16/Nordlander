from django.shortcuts import render
from featuresAndBugs.models import FeaturesAndBugs

# Create your views here.
def do_search(request):
    featuresAndBugs = FeaturesAndBugs.objects.filter(name__icontains=request.GET['search'])
    return render(request, "featuresAndBugs.html", {"featuresAndBugs": featuresAndBugs})
