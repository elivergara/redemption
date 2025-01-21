from django.shortcuts import render, get_object_or_404, redirect
from .models import PlannerEvent
from .forms import PlannerEventForm

# List all events for the year
def planner_list(request):
    events = PlannerEvent.objects.order_by('datetime')
    return render(request, 'planner_list.html', {'events': events})

# Add a new event
def add_event(request):
    if request.method == 'POST':
        form = PlannerEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planner_list')
    else:
        form = PlannerEventForm()
    return render(request, 'add_event.html', {'form': form})

# Edit an existing event
def edit_event(request, pk):
    event = get_object_or_404(PlannerEvent, pk=pk)
    if request.method == 'POST':
        form = PlannerEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('planner_list')
    else:
        form = PlannerEventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

# Delete an event
def delete_event(request, pk):
    event = get_object_or_404(PlannerEvent, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('planner_list')
    return render(request, 'delete_event.html', {'event': event})
