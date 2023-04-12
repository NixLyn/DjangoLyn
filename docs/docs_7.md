# AUTH CONTROL #

# NavBar #

Now that we have a way to Register/Login/Logout,
we should let our user be aware of the session state.

In your where you wrote your navbar codes (mine is in 'base.html')
Make these changes:

```
<nav>
    {% if user.is_authenticated %}
    <a class="to_dash"> <<-- This is for later..
        <div>My Dash</div>
    </a>
    <a class="new_post" href="{% url 'add_post' %}">
        <div>New Post</div>
    </a>
    <a class="sign_in" href="{% url 'logout' %}">
        <div>Sign-Out</div>
    </a>
    {% else %}
    <a class="sign_in" href="{% url 'login' %}">
        <div>Sign-In</div>
    </a>
    <a class="sign_up" href="{% url 'register' %}">
        <div>Sign-Up</div>
    </a>
    {% endif %}
</nav>
```

You can apply the same logic to all areas of the project

## User Restriction ##

But if you want to make sure users are only able to edit/delete only their own
then we need to compare the user id to the post_author id.
Luckily django provides means of doing this.

Here's an example:
```
<h2> Current User ID : {{ user.id }}        </h2>
<h2> Post User Id    : {{ post.author.id }} </h2>
```

So we use..
```
{% if user.id == post.author.id %}
```

And here is a more practical example:

```
<!-- First We check if the user is logged in -->
{% if user.is_authenticated %}
    <!-- Then we check if the ids match -->
    {% if user.id == post.author.id %}
        <h1>
            Delete {{ post.title }} ?!
        </h1>
        <div class="form-group">
            <form method="POST">
                {% csrf_token %}
                {{ form.as_p }}
                <strong>
                    [DELETING] : ARE YOU SURE ?
                </strong>
                <button>Delete</button>
            </form>
        </div>
    {% endif %}
{% else %}
<h1>
    You are not autherized to delete this post
</h1>
```

## Profiles ##

The rest of this documentation will not include all the profile changes.
You can find more on it buy following John Elder in this tutorial:
<a href="https://www.youtube.com/watch?v=Nxgi4qF6i1Q&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=24">

The next documentation will cover the basics of the DashBoards and Connecting the user to
the corrosponding ToolBoxNodes, so we can run scripts and return the data to user for view, 
as well as saving the retrieved data to a database.

Afterwards a  segmentation on Security Analysis of Django vs Recons
