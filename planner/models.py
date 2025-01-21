from django.db import models

class PlannerEvent(models.Model):
    title = models.CharField(max_length=200)
    where = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True) 
    datetime = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    contact = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, blank=True, null=True, help_text="Optional one-line description")
    def __str__(self): 
        return f"{self.title} ({self.date or self.datetime})"