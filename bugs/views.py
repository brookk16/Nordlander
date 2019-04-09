from django.shortcuts import render
from .models import Bugs

# Create your views here.
def all_bugs(request):
    bugs = Bugs.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})