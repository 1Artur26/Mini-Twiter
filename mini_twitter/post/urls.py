from django.urls import path
from .views import  post_list, add_post, add_comment, view_comments, post_detail

urlpatterns = [
    path('posts/<str:username>/', post_list, name='post_list_by_user'),
    path('posts/', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('post/<int:post_id>/comments/', view_comments, name='view_comments'),
]