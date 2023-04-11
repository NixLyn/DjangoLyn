# Authentication #

Finally... we will now make start the app for use authentication

# StartApp #
So first things first:

```
python manager.py startapp members
```
### Settings ###

You can name the app whatever you'd like, I just used members

Then you can add the new app to your setting.py file:

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
    'members',
]


# And _DOWN_ at the bottom add the following:

LOGIN_REDIRECT_URL = 'homepage'
LOGINOUT_REDIRECT_URL = 'homepage'

# We'll need them later
```


### Site/Urls ###

We will also need to all the url path in the main urls.py:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]

```

### Members/Urls ###

Django has some cool built-in tools to help us with this process
Now that the urls have been sorted on the main project files
Let's go to  'members/ ' and make a 'urls.py' file.
(You can even copy+paste the homepage/urls.py, then make these changes)


```
from django.urls import path
from .views import UserRegisterView

# We will not need a 'login' url, because django is cool/weird like that

urlpatterns = [
    path('register/',   UserRegisterView.as_view(),     name='register'),
]

```

### Views ###

In our 'members/view.py' file:

```
from django.shortcuts import render
from django.views import generic

# Django's predefined Authentication method + view
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# The object well call in the urls.py file
class UserRegisterView(generic.CreateView):
    form_class      = UserCreationForm
    template_name   = 'registration/register.html'
    # Redidrect new users to login page
    success_url     = reverse_lazy('login')

```

### html ###

First We can add links for Register & Login in the 'base.html' navbar:

```
<a class="sign_in" href="{% url 'login' %}">
    <div>Sign-In</div>
</a>
<a class="sign_up" href="{% url 'register' %}">
    <div>Sign-Up</div>
</a>
```

Notice that 'login' redirect will work correctly, be default:

In 'memebers/templates/registration/':
We can make our 'register.html' and 'login.html' files:

The {% extends 'base.html' %} will 
automatically find the original base.html
in later parts of this project, we will 
use a different base as not all areas of 
the site will have the same nav functions

Register.html
```
{% extends 'base.html' %}
{% block title %}Register{% endblock %}

{% block content %}
{% load static %}
<section class="all_back">
    <h1>
        Register To NixLyn_Lab
    </h1>
    <div class="form-group">
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button>Register</button>
        </form>
    </div>
</section>
{% endblock %}

```

Login.html

```
{% extends 'base.html' %}
{% block title %}Login{% endblock %}

{% block content %}
{% load static %}
<section class="all_back">
    <h1>
        Login To NixLyn_Lab
    </h1>
    <div class="form-group">
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}  
            <button>Login</button>
        </form>
    </div>
</section>
{% endblock %}
```

### RunDown ###

We new have the base functionality for auths:
Next up we will need to make use of this user-auth tool,
So we'll be making some changes to the code to control
who can/can't do what, depending on their account..


Your 'members' directories tree should now look like this:

```
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.*.pyc
├── models.py
├── __pycache__
│   ├── *.pyc
├── templates
│   └── registration
│       ├── login.html
│       └── register.html
├── tests.py
├── urls.py
└── views.py
```
