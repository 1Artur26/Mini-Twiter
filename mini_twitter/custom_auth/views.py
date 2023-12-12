from django.urls import reverse_lazy
from django.views import generic
from custom_auth.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.http import JsonResponse
from post.models import Post


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'custom_auth/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        
        context = super(ProfileView, self).get_context_data(**kwargs)
        
        
        followers = self.request.user.followers.all()
        context['followers_posts'] = Post.objects.filter(user__in=followers)

        return context
    

class CustomLoginView(LoginView):
    template_name = 'custom_auth/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  
    template_name = 'custom_auth/register.html'


class UserListView(ListView):
    model = CustomUser
    template_name = 'custom_auth/user_list.html'  
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'custom_auth/user_detail.html'
    context_object_name = 'user'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main')


@login_required
def toggle_follow(request, user_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if request.user in user_to_follow.followers.all():
                user_to_follow.followers.remove(request.user)
                followed = False
            else:
                user_to_follow.followers.add(request.user)
                followed = True

            return JsonResponse({'followed': followed}, status=200)

        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'custom_auth/edit_profile.html', {'form': form})



class FollowersListView(ListView):
    model = CustomUser
    template_name = 'custom_auth/followers_list.html'
    context_object_name = 'followers'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        return user.followers.all()

    def get_context_data(self, **kwargs):
        context = super(FollowersListView, self).get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        context['user'] = get_object_or_404(CustomUser, id=user_id)
        return context
    

class FollowingListView(ListView):
    model = CustomUser
    template_name = 'custom_auth/following_list.html'
    context_object_name = 'following'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        return user.following.all()

    def get_context_data(self, **kwargs):
        context = super(FollowingListView, self).get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        context['user'] = get_object_or_404(CustomUser, id=user_id)
        return context