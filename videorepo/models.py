from django.db import models


# Create your models here.
class VideoItem(models.Model):
    thumb_url = models.CharField(max_length=5120, blank=True)
    url = models.CharField(max_length=5120)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

