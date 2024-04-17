from rest_framework  import serializers
from .models import YouTubeVideos

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideos
        fields = ('title', 'channel', )