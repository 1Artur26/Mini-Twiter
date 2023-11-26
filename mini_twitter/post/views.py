from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from users.models import  User
from .forms import PostForm, CommentForm

def post_list(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(user=user)
    else:
        posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  
    else:
        form = PostForm()
    return render(request, 'post/add_post.html', {'form': form})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'post/add_comment.html', {'form': form, 'post': post})


def view_comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post/comment_list.html', {'post': post, 'comments': comments})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', {'post': post})

