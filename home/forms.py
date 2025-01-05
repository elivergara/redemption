from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Event

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Events form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'pushpay_link']  # Added pushpay_link


