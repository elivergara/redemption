from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image8 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image9 = models.ImageField(upload_to='news_images/', null=True, blank=True)
    image10 = models.ImageField(upload_to='news_images/', null=True, blank=True)