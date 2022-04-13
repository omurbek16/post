from .models import Post, Comments
from .serializers import PostSerializer, CommentsSerializer
from django.views.generic import ListView, DetailView
from rest_framework import viewsets


class PostListView(ListView):
    model = Post
    template_name = "post/postlist.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
