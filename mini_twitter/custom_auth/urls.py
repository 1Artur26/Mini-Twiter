from django.urls import path
from .views import RegisterView, CustomLoginView, ProfileView, UserListView, UserDetailView, edit_profile, toggle_follow, FollowersListView, FollowingListView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('toggle-follow/<int:user_id>/', toggle_follow, name='toggle_follow'),
    path('users/<int:user_id>/followers/', FollowersListView.as_view(), name='followers_list'),
    path('users/<int:user_id>/following/', FollowingListView.as_view(), name='following_list'),
    path('logout/', LogoutView.as_view(), name='logout'),  
]