from django.db import models
from django.utils import timezone

class Activity(models.Model):
    name = models.CharField(max_length=15, blank=False)
    description = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    owner = models.ForeignKey('auth.User', related_name='activity', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']