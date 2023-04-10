# Basic Base Layout #

In order to simplify things like universal NavBars,
we use something known as {% extends 'base.html' %}


## Design Tree ##

Beside the templates folder, web designers often use the 'static' folder
which contains something:

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
    <link rel="stylesheet" href="../static/css/nav.css"/>
    <link rel="stylesheet" href="../static/css/base.css"/>
    <title>NixLyn_Labs</title>
</head>
<body>
    <nav>
        <div class="mNav">
            <a href="../"><div class="logo">
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
    <link rel="stylesheet" href="../static/css/homepage.css"/>
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
    <link rel="stylesheet" href="../static/css/detailed.css"/>
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



## Style It ##

You can now edit your css to your hearts content, or copy paste from bootstrap..
but those are outside the scope of this tutorial

Next up we will make it possible to add a post on the noticeboard

