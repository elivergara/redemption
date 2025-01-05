from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_to_updates = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/events/', blank=True, null=True)  # Optional image field
    pushpay_link = models.URLField(max_length=500, blank=True, null=True)  # New optional hyperlink field
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
