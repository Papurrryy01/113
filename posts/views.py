from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Status

# Create your views here.

def _get_status_queryset(status_name):
    status = Status.objects.filter(name__iexact=status_name).first()
    if not status:
        return Post.objects.none()
    return Post.objects.filter(status=status).order_by("-created_on")


class PostPublishedListView(ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return _get_status_queryset("published")


class PostDraftListView(ListView):
    template_name = "posts/draft_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return _get_status_queryset("draft")


class PostArchivedListView(ListView):
    template_name = "posts/archived_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return _get_status_queryset("archived")


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "author", "status"]

    def form_valid(self, form):
        print(User.objects.all())
        form.instance.author = self.request.user
        return super().form_valid(form)


# --mini challenge--
class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "posts/post_update.html"
    model = Post
    fields = ["title", "subtitle", "body", "author"]


class PostDeleteView(DeleteView):
    template_name = "posts/post_delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostListView(PostPublishedListView):
    pass
