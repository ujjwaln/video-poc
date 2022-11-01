from rest_framework import serializers
from videorepo.models import VideoItem


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItem
        fields = ["url", "description", "title"]

