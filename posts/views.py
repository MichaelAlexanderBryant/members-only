from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "home.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)