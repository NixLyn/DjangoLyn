## Let's Make A SuperUser ##

```!/bin/bash
$ python manage.py createsuperuser
```

Enter your desired username and press enter.

```!/bin/bash
Username: admin
```

You will then be prompted for your desired email address:

```!/bin/bash
Email address: admin@example.com
```

Then prompted to type in a PassWord.. twice

..Save it somewhere.. [I've had to redo projects because I couldn't remember mine..]

Then go ahead and run:

```!/bin/bash
$ python3 manager.py makemigrations

$ python3 manager.py migrate

$ python3 manager.py runserver
```

Make your way to the browers and go to

### 127.0.0.1:8000/admin/ ###

There you will login again, and if all goes well
you should see a page like this one:

<img src="pics_/admin_post_login.png">

### Next up, you can start making your first Home Page ###

First we will need to create an app:

```!/bin/bash
$ python manager.py startapp homepage
```

You Should now see a directory tree like this:

<img src="pics_/DjangoTree_2Apps.png">

If you are to run the server before the next steps, you should see something like:

<img src="pics_/noticeBoard_NoIndex.png">

If so, in the 'homepage/views.py' file add:

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the HomePage index.")
```

Then we call views in the 'homepage/urls.py' file and add:

```
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

And finally, in the 'NixLyn_Lab/ursl.py' we will change:

```
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

by adding:

```
urlpatterns = [
    path("homepage/", include("homepage.urls")),
    path('admin/', admin.site.urls),
]
```

Now, run the server again:

```!/bin/bash
$ python3 manager.py makemigrations

$ python3 manager.py migrate

$ python3 manager.py runserver
```

and go on over to:

### 127.0.0.1:8000/homepage/ ###

in your browers, and if all went well you will see:

<img src="pics_/WithBase_Index.png">


### ClosingNotes ###

Some thing s might not corrospond, as I first started with 'noticeBoard' then messed up,
So restarted with a simple 'homepage'...