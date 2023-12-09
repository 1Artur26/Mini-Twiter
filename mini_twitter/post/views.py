from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views import View

class PostListView(ListView):
    model = Post

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = get_user_model().objects.get(pk=self.request.user.pk) 
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/add_comment.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.user = get_user_model().objects.get(pk=self.request.user.pk) 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_list')


class CommentListView(ListView):
    model = Comment
    template_name = 'post/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    

class MainPageView(TemplateView):
    template_name = 'post/base.html'



class ToggleLikeView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('post_detail', post_id=post_id)
    

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/edit_post.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/confirm_delete.html'
    success_url = reverse_lazy('post_list')

