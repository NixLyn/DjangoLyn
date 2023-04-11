from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

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
    ordering        = ['-id']

class UpdatePostView(UpdateView):
    model           = Post
    form_class      = EditForm
    template_name   = 'update_post.html'
    success_url = reverse_lazy('homepage')

class DeletePostView(DeleteView):
    model           = Post
    template_name   = 'delete_post.html'
    fields          = '__all__'
    success_url = reverse_lazy('homepage')

