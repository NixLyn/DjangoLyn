from django.shortcuts import render
from django.views.generic import ListView, DetailView
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

