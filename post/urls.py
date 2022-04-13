from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostView,
    CommentsView,
)


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"post", PostView)
router.register(r"comments", CommentsView)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("api/v1/", include(router.urls)),
]
