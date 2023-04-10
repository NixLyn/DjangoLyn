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

<section>
    <h1> Hello World </h1>
    <p> 
        My HomePage, with an extended base. This base will be present in each
        page that I extend it in
    </p>
</section>

{% endblock %}
```


## Style It ##

You can now edit your css to your hearts content, or copy paste from bootstrap..
but those are outside the scope of this tutorial

Next up we will make it possible to register and login
