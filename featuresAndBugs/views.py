from django.shortcuts import render
from .models import FeaturesAndBugs

# Create your views here.
def all_features_and_bugs(request):
    featuresAndBugs = FeaturesAndBugs.objects.all()
    return render(request, "featuresAndBugs.html", {"featuresAndBugs": featuresAndBugs})
