# User DataBase #

Now that we have our homepage setup, we want users to be able to
Register and Login, so let's make a database for them

This means some auth tools are in order..

in the 'homepage/models.py' file:

```!/bin/bash
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    add_on = models.TextField(max_length=255, default="ADD_FUNDS")
    date_made  = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.title) + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('home', )
```

Now in your 'homepage/admin.py' add :

```!/bin/bash
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

And you can now run the server and go to the '/admin' in your browers
if all goes well, you should see:

<img src="pics_/NewDB_Post.png">

Which means that we will be able to link users to posts
but first, let's stop the server and makemigrations

```!/bin/bash
python manage.py makemigrations
```

```!/bin/bash
python manage.py migrate
```

```!/bin/bash
python manage.py runserver
```

Then head on over to the '/admin' in your browers:


<img src="pics_/create_post.png">

You will see there is the option to add a post :)

<img src="pics_/make_post.png">

