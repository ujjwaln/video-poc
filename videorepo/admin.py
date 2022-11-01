from django.contrib import admin
from videorepo.models import VideoItem


@admin.register(VideoItem)
class VideoItemModelAdmin(admin.ModelAdmin):
    pass
