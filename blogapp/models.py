from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    dated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
