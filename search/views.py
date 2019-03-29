from django.shortcuts import render
from featuresAndBugs.models import FeaturesAndBugs

# Create your views here.
def do_search(request):
    products = FeaturesAndBugs.objects.filter(name__icontains=request.GET['q'])
    return render(request, "featuresAndBugs.html", {"featuresAndBugs": featuresAndBugs})
