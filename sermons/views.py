
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sermon
from .forms import SermonForm



def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def add_sermon(request):
    if request.method == 'POST':
        form = SermonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latest_sermon')  # Redirect to the latest sermon page
    else:
        form = SermonForm()
    return render(request, 'sermons/add_sermon.html', {'form': form})


# def latest_sermon(request):
#     latest = Sermon.objects.order_by('-created_at').first()
#     return render(request, 'sermons/latest_sermon.html', {'sermon': latest})

def latest_sermon(request):
    # Fetch the two most recent sermons
    sermons = Sermon.objects.all().order_by('-created_at')[:2]  # Get the two most recent sermons
    sermon_1 = sermons[0] if sermons else None
    sermon_2 = sermons[1] if len(sermons) > 1 else None

    return render(request, 'sermons/latest_sermon.html', {
        'sermon_1': sermon_1,
        'sermon_2': sermon_2,
    })




# Edit sermon view
def edit_sermon(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    if request.method == 'POST':
        form = SermonForm(request.POST, instance=sermon)
        if form.is_valid():
            form.save()
            return redirect('latest_sermon')  # redirect to the watch page or another relevant page
    else:
        form = SermonForm(instance=sermon)
    return render(request, 'sermons/edit_sermon.html', {'form': form})

# Delete sermon view
def delete_sermon(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    sermon.delete()
    return redirect('latest_sermon')  # redirect to the watch page or another relevant page