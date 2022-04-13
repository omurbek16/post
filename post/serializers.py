from .models import Post, Comments
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "body", "author", "date_posted"]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["post", "author", "body", "date_added"]
