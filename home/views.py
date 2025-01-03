from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event
from .forms import EventForm
from django.contrib.auth.models import Group


# Create your views here.
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login
            messages.success(request, f'Account created for {user.username}!')
            return redirect(reverse('profile'))
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})


from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'home/profile.html')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def latest_sermon(request):
    return render(request, 'sermons/latest_sermon.html')

def blog(request):
    return render(request, 'home/blog.html')


def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page

@login_required
def update_subscription(request):
    if request.method == 'POST':
        # Get the checkbox value (True if checked, otherwise False)
        subscribe_updates = 'subscribe_updates' in request.POST
        
        # Update the user's profile
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.subscribed_to_updates = subscribe_updates
        profile.save()
        
        # Optionally, add a success message
        from django.contrib import messages
        messages.success(request, "Your preferences have been updated.")
        
    return redirect('profile')  # Redirect back to the profile page


######### Events Adding/Editing Section
def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm(instance=event)
    return render(request, 'home/edit_event.html', {'form': form, 'event': event})

@login_required
@user_passes_test(is_staff_user)
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return render(request, 'home/delete_event.html', {'event': event})

def events_list(request):
    events = Event.objects.all().order_by('-created_at')  # Query all events
    is_staff = request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name='Staff').exists())
    return render(request, 'home/events.html', {'events': events, 'is_staff': is_staff})
