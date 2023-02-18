from django.urls import path

from .views import PostListView, PostCreateView

urlpatterns = [
    path("newpost/", PostCreateView.as_view(), name="new-post"),
    path("", PostListView.as_view(), name="home")
]