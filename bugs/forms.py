from django import forms
from .models import Bugs

class AddBugForm(forms.ModelForm):
    
    
    class Meta:
        model = Bugs
        fields = (
            'name', 'description', 'type', 
        )