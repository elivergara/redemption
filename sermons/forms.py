from django import forms
from .models import Sermon

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'embed_link']
        widgets = {
            'embed_link': forms.Textarea(attrs={'rows': 3}),
        }
