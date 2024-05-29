from django import views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    # import other views as needed
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add-blog/',views.AddBlog.as_view(), name='add_blog'),
    # Add other URL patterns for your blog app here
]
