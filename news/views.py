from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm

# View for adding news
def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save(commit=False)  # Create object but don't save to DB
            news_item.author = request.user     # Set the author to the logged-in user
            news_item.save()                    # Save the object to the database
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

# View for listing news
def news_list(request):
    news_articles = News.objects.all().order_by('-created_at')  # Fetch all news, newest first
    return render(request, 'news_list.html', {'news_articles': news_articles})

# View for editing news
def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)  # Fetch the news by primary key
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()  # Save the updated news
            return redirect('news')  # Redirect to the news listing page
    else:
        form = NewsForm(instance=news)
    return render(request, 'edit_news.html', {'form': form, 'news': news})

# View for deleting news
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)  # Fetch the news by primary key
    if request.method == 'POST':
        news.delete()  # Delete the news item
        return redirect('news')  # Redirect to the news listing page
    return render(request, 'delete_news.html', {'news': news})
