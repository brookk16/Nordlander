from django.shortcuts import render
from .models import Features

# Create your views here.
def all_features(request):
    features = Features.objects.all()
    return render(request, "features.html", {"features": features})
