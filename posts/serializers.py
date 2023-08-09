from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Post
        fields = ['id','title', 'image', 'caption', 'typ']