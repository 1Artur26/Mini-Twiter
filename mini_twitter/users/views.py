from django.shortcuts import render, get_object_or_404
from .models import User
from post.models import Post

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/user_detail.html', {'user': user, 'posts': posts})
