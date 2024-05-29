from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from django.views import View
from django.views.generic import LoginView

# Create your views here.
class PostList(ListView):
    model=Post
    context_object_name='list'
    template_name="registration/blog.html"
class LoginView(LoginView):
    form_class=AuthenticationError
    authentication_form=None
    template_name="registration/login.html"
    redirect_authenticated_user=False
    extra_content=None
class Addlog(CreateView):
    model=Post
    form_class=PostForm
    template_name='registration/login.html'
