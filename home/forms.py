from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from .models import AboutPage

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

#Events form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_date', 'description', 'image', 'pushpay_link', 'map_embed']  
        widgets = {
    'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Allows input in datetime-local format
}

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__' 
        # fields = [
        #     "title_en",
        #     "subtitle_en",
        #     "subtitle_es",
        #     "service_times_en",
        #     "contact_name",
        #     "contact_email",
        #     "contact_address",
        #     "mission_en",
        #     "mission_es",
        # ]
        # widgets = {
        #     "subtitle_en": forms.Textarea(attrs={"rows": 2}),
        #     "subtitle_es": forms.Textarea(attrs={"rows": 2}),
        #     "service_times_en": forms.Textarea(attrs={"rows": 4}),
        #     "mission_en": forms.Textarea(attrs={"rows": 6}),
        #     "mission_es": forms.Textarea(attrs={"rows": 6}),
        # }