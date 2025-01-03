
# Create your views here.
from django.shortcuts import render, redirect
from .models import Sermon
from django.contrib.auth.decorators import login_required, user_passes_test
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
            return redirect('sermons')
    else:
        form = SermonForm()
    return render(request, 'sermons/add_sermon.html', {'form': form})

def latest_sermon(request):
    latest = Sermon.objects.order_by('-created_at').first()
    return render(request, 'sermons/latest_sermon.html', {'sermon': latest})
