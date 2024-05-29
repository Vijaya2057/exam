from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, LoginView, DeleteView
from .forms import PostForm  # Assuming you have a PostForm defined in forms.py
from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = 'list'
    template_name = "registration/blog.html"

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_content = None

class AddBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'registration/add_blog.html'
    success_url = reverse_lazy('blog')

class UpdateBlog(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'registration/update_blog.html'
    success_url = reverse_lazy('blog')

class DeleteBlog(DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'registration/update_blog.html'
    

