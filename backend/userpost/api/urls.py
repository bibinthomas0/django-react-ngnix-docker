from django.urls import path
from . import views



urlpatterns = [
path('posts/', views.UserPosts.as_view(), name='listing-post'),
        path('posts/create', views.CreatePostViewSet.as_view(),name="create-post"),
]