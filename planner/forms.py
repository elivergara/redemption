from django import forms
from .models import PlannerEvent

class PlannerEventForm(forms.ModelForm):
    class Meta:
        model = PlannerEvent
        fields = ['title', 'description', 'datetime', 'contact']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
