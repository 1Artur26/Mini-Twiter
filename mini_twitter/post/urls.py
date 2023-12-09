from django.urls import path
from post.views import  PostListView, AddCommentView, AddPostView, PostDetailView, CommentListView, ToggleLikeView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:post_id>/comments/', CommentListView.as_view(), name='view_comments'),
    path('post/<int:post_id>/toggle_like/', ToggleLikeView.as_view(), name='toggle_like'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]