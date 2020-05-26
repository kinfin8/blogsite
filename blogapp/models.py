from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def preview(self):
        return self.content[0:self.content.find("</div>")+6]