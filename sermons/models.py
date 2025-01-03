from django.db import models

# Create your models here.

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    embed_link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
