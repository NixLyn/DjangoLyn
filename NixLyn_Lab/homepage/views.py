from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

# Create your views here.
#def homepage(request):
#    return render(request, 'homepage.html', {})

class HomeView(ListView):
    model           = Post
    template_name   = 'homepage.html'

class ArticleDetailView(DetailView):
    model           = Post
    template_name   = 'article_details.html'

class AddPostView(CreateView):
    model           = Post
    template_name   = 'add_post.html'
    fields          = '__all__'

class UpdatePostView(UpdateView):
    model           = Post
    template_name   = 'add_post.html'
    fields          = '__all__'
