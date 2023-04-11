# Basic Base Layout #

In order to simplify things like universal NavBars, we use something
 known as "base" files, an example of it looks like this:

``` 
{% extends 'base.html' %}
{% block content %}

...some html here...

{% endblock %}
```

## Design Tree ##

Beside the templates folder, Web developers/designers often use the 'static' folder,
which looks something like:

```
.
├── css
│   ├── base.css
│   ├── homepage.css
│   ├── nav.css
├── images
├── js
│   ├── base.js
└── pics
    ├── picture_1.jpg
    ├── picture_2.jpg
    ├── picture_3.jpg
```

To seperate all the different types of purposes.. html (structure), js (functions), css (style),

This is a we structured way of keeping everything organized:
(PS: never put any actual pictures in the 'images' folder.. that is for other things)

## Base.html ##

in 'templates/base.html' create your base template, mine looks kind of like this:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static '../static/css/nav.css' %}"/>
    <link rel="stylesheet" href="{% static '../static/css/base.css' %}"/>
    <title>NixLyn_Labs</title>
</head>
<body>
    <nav>
        <div class="mNav">
            <a href="{% url 'homepage' %}"><div class="logo">
                <h1>NL</h1>
            </div></a>
            <div class="signing">
                <div class="sign-in">
                    <a>Sign_In</a>
                </div>
                <div class="sign-up">
                    <a>Sign_In</a>
                </div>
            </div>
        </div>
    </nav>
    
    {% block content %}

    {% endblock %}
    
</body>
</html>
```

Now in the 'templates/homepage.html' you can extend this base:

```
{% extends 'base.html' %}

{% block content %}
    <link rel="stylesheet" href="{% static '../static/css/homepage.css' %}"/>
    <section class="post_sect">
        <h1 class="post_head_line">NoticeBoard</h1>
        <!-- USING JINJA -->
        <div>
            <ul class="post_head">
                {% for post in object_list %}
                <div class="post_block">
                    <a href="{% url 'article-details' post.pk %}">
                        <li>{{ post.title }}</li>
                        <li>{{ post.author }}</li>
                        <li>{{ post.body }}</li>
                        <br>
                    </a>
                </div>
                <br>
                {% endfor %}
                <br>
            </ul>
        </div>
    </section>
{% endblock %}
```

Having used href="{% url 'article-details' post.pk %}"

You will be able to click on the any of the posts
and be redirected to the detailed-article page..

```
{% extends 'base.html' %}

{% block content %}
{% load static %}
    <link rel="stylesheet" href="{% static '../static/css/detailed.css' %}"/>
    <section class="all_back">
        <h1>
            Article Details
        </h1>
        <div class="daBlock">
            <h1>{{ post.title }}</h1>
            <h2>{{ post.author.first_name }}</h2>
            <h2>{{ post.author.last_name }}</h2>
            <h2>{{ post.author.email }}</h2>
            <h3>{{ post.body }}</h3>
            <h4>{{ post.add_on }}</h4>
        </div>
    </section>
{% endblock %}
```

Next page we will make it possible to add/update/delete a post on the noticeboard.


### Style It ###

You can now edit your css to your hearts content, or copy paste from bootstrap..
but those are outside the scope of this tutorial, and for the sake of keeping this
tutorial as simplistic as possible, I won't be including them in the docs,
unless otherwise required for the sake of achieving a goal..



### ClosingNotes ###

If ever I do make another one of these bad-grammered, miss-spelled, late-night, docs
on such a topic, it will be isolated from other engagements. As it has been pointed out to me,
that I do need to learn to stay on topic...

Like that other time we started building a rando...
