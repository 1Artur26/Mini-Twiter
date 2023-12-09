from django.contrib import admin
from django.urls import path, include 
from post.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view() , name='main'),
    path('post/', include('post.urls')),
    path('user/', include('custom_auth.urls')),
]
