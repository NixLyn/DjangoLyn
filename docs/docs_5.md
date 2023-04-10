# Add Posts #

Now that we can view a list of our noticeboard posts
and view them in detail, let's make it possible for our
users to add a post


in 'homepage/views.py' add:

```
from django.views.generic import ListView, DetailView, CreateView


class AddPostView(CreateView):
    model           = Post
    template_name   = 'add_post.html'
    fields          = '__all__'

```

in the 'homepage/urls.py' add:

```
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add_post')
]
```


In 'homepage/models.py' add:


```
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    ...

    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))
```


Great, You can now add a new post!

### Some Styli-sh ###

create a 'forms.py' in the 'homepage' folder:

```
```
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'add_on': forms.TextInput(attrs={'class': 'form-control'}),
        }
```

Then from here, off to bootstrap for some easy form styling...
