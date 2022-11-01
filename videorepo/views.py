from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from videorepo.serializers import VideoItemSerializer, VideoItem


class VideoItemViewset(viewsets.ModelViewSet):
    queryset = VideoItem.objects.all()
    serializer_class = VideoItemSerializer
    # filter_backends = [ DjangoFilterBackend ]
    # filterset_fields = ['id', 'title']
    permission_classes = (AllowAny, )

