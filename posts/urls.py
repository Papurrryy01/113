from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostPublishedListView.as_view(), name="post_list"),
    path("drafts/", views.PostDraftListView.as_view(), name="post_draft_list"),
    path("archived/", views.PostArchivedListView.as_view(), name="post_archived_list"),
    path("new/", views.PostCreateView.as_view(), name="create_post"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    # --mini challenge--
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]
