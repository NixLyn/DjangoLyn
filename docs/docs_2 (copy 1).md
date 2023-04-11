# First A HomePage #

To create the 'homepage' app, in the project base directory
We'll need to run this command:

```!/bin/bash
$ python manage.py startapp homepage
```

If no errors appear, it worked

## Settings ##

Now to add the module to the setings open 'NixLyn_Lab/settings.py'
and make these changes:

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',                     <<--
]
```

## Migrate ##

Since we have the login database already setup for /Admin
we can simply migrate the app's configs with a simple command in the base directory

```!/bin/bash

$ python manage.py makemigrations

$ python manage.py migrate
```

It should respond with :

```!/bin/bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

## Base:URLS ##

We'll need to add these changes to the 'NixLyn_Lab/urls.py' file:

```
from django.contrib import admin
from django.urls import path, include               <<-- 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")), #   <<-- 'homepage urls link'
]
```

### HomePage:URLS ###

Now in the 'homepage/' directory, create a 'urls.py' file
and add:

```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
```

## Views ##

In the 'homepage/vies.py' file you will need:

```
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})
```

### HomePage:HTML ###

Almost every WebDesign platform uses 'templates/' folders to hold their html file,
Django is no different..

so in the 'homepage/' directory, make a folder named templates
and in there we can make the 'homepage.html' file, which the views.py will point to

A simple "Hello World!" is always a good start:

```
<h1>Hello World!</h1>
```

Next, once again:

```!/bin/bash
$ python manage.py runserver
```

Now `http://127.0.0.1:8000/` should be your home directory page in the browers

### ClosingNotes ###

It's Always _BEST_ Practice to work [BACK] to [FRONT]..
With the case of Django:
-> ```models.py```
-> ```forms.py```
-> ```views.py```
-> ```urls.py```
-> ```.html```
-> ```.css```
-> ```.js```

