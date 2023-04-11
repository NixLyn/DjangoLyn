# Basics of Django #

My Point of View:

    Django is a FreeToUse framework, for FullStack development of scalable projects.
it is very popular due to almost 'API' like structure and behaviour. It allows for 
built-in `sqlite3`, which is a massive cost saving tool, espescially for newer devs,
or devs learning something new, as sql can be expansive (and sometimes, rediculously slow,
even more so, when like me.. you have no idea how that $#@! works..).
    One of the great freaturs of django is it 'Jinja'-like style of usage in html, though 
a bit limited, still quite handy, as it tends to mostly follow the same basic rules of 'Jinja'.
One of the main reasons why so many use Django is because of it's ablity to run on even the most
basic of hardware, (even my 15 yewar-old, celron, 4gb/ram..). After having done a flask project
for freelance project (in efforts to save money, given the requirements of the client..), I learn
about Django and it's expansive capacity, and lite-ness. Not only is Django capable of integrating
with candy codes like 'ReactJs', but it's tolerance for backend flexablity has left me 
star-gazing... 

My Intentions with This Project:

    Seeing that Django is only game for just about any WebApp FrontEnd style you might think of.
But also has some 'API'-ish ways, I figured I would start a project with it again, but this time,
actually do my documentation (I blame Frankie Thomas, THM Top 1%, who inspired me with the way 
he went from zero to hero in under a year, Thanks man). The purpose of the documentation is not 
only just so I can quickly look back, when I forget stuff, and not only to be able to help anyone 
who joins the NixLyn Community, but also to start diving into the belly of the notorious little
Beast.. Seeing how it is so widely used even in corporate companies, I figured I would start by 
first building a project, where I research every potential vulnerablity/weakness/exploit/gap/etc...
Then, run it on a seperate system, where Frankie and I will start using it as "[TargetPractice]"
Hence honing not just the skills in development, but also in understanding the methods and techniques
of hacking and hopefully creating solutions to the security risks.. 
```
Build, Break, Strengthen, repeat..
```

Hopes For The '[Final]' Product:

    Hopefully, by the end of this project there will be: 
    ~Secure Authentication (Price Effective Means)
    ~Elegant Templates, Smooth Design
    ~A NoticeBoard (Which is actually just for the purpose of the excercise..)
    ~DashBoard Containing:
        -> A) ReconRoom  (Active)    : Fundemental tools for target enumeration
        -> B) ReconRoom  (Passive)   : Continual Port Listening (With my own version of 'T-Shark') 
        -> C) BruteBench (Basics)    : Tools ranging from hydra to SQL_injection, along with my 'Site-Clone'
        -> D) VunlsTuri  (Scan&enum) : A stack of every possible method of scanning for vulnerablities
        -> E) XploiTier  (X-Stacks)  : All your XSS, XML, SSI, XPATH, IMAP/SMTP, SSL, HHI, SSRF, SAML, etc
        -> F) FiringRange(VM_Clone)  : Automated config/build of target specs on a VM from all InfoSecData
        -> G) GraPhickle (Report'n)  : Graphical results + stage_list report generating of final results
    ~Frankenstein's Secrets (Frankie's Labs) :
        -> A) [Journal] - PDF Documentation(s) on his extensive research in the field
        -> B) [PodCast] - Schedules, Downloads, LiveLinks, ..?
        -> C) [Honing_] - Community Blog for QnA, Book 1-on-1 *TryHackMe* tutoring sessions/lessons
        -> D) [Social_] - Testimonials on the reality of Social Media as a Marketing platform
        -> E) [PubNubs] - Buy/PreOrder Frankie's Latest books on the plunders of ```Rooting & Looting```
        -> F) [BugHunt] - Watch Snippets of our funniest moments during our *Hunting Trips* (No-Code)
        -> G) [GainLyn] - Get a potential interview, to join the NixLyn_Dev team, (aka. the $#!T_S#0W)
    ~CLI_ to API: (for the DieHard_TerminalJunkies) Use Our CLI, which includes a range of step-by-step
        explainations on the fundamentals of the process behind the `automated hacking` process.
    ~RedvsBlue: Community Configured Events for those looking to practice, learn, share, root&loot...


...If you actually read through all that, just know I didn't proof-read it, just splashed it on there,
and thruth be told, not sure it gets any better from here. But, thanks for checking this out, really hope
you enjoy it. It was quite time consuming, and I did it with the best of intentions.

~~Not gonna wait for the credits to give a special thanks to <link href="https://www.youtube.com/@Codemycom">_John Elder_</a> From _codemy.com_ for all the great material,
you guys can look him up on YouTube, Hoping to see more from him, as he does bring forth some great content, and I 
truelly wuld not have been able to do this project had it not been for him (Actually, even the Flask project which paid rent)
Please, give him some support <a href="https://codemy.com/">_CodeMy.com_</a>..<3


Please Note: This Documentation does not include the styles.css, I will make one document Explaining the basics,
    but from there, I believe creativity is something which must come, both,  _from the heart_ & _hard work_
    though all my source codes will be up on A public Repo, do your best to beat the rest, Would love to see 
    what you guys come up with, please share some screenshots and links in the NixLyn Community Forum.. <3


OK, I'm done,not to get back to work...

# Getting Started #


Please, make sure to save your work, I prefer GitHub..
..but you do you..

## Setup virtual environment ##

```!/bin/bash
$ virtualenv d_env
```

## Activate The Env ##

```!/bin/bash
$ source d_env/bin/activate
```

## Install needed packages ##

```!/bin/bash
$ pip install django

$ python -m pip install django-htmx django-htmx-refresh

$ pip install django_quill

```

## Check the django version ##

```!/bin/bash
$ python -m django --version
```

## Create Project ##

```!/bin/bash
$ django-admin startproject mysite 
```

^ In my Case I used "NixLyn_Lab" ^

## Project Structure Basic ##

<img src="pics_/django_project_base_tree.png">

```!/bin/bash
$ tree

mysite/
    manage.py           [A]
    mysite/             [B]
        __init__.py     [B.1]
        settings.py     [B.2]
        urls.py         [B.3]
        asgi.py         [B.4]
        wsgi.py         [B.5]

```


## These Files Are ##

-[A] manage.py: A command-line utility that lets you interact with this Django project in various ways.
    ~You can read all the details about manage.py in django-admin and manage.py.
    <a href="https://docs.djangoproject.com/en/4.2/ref/django-admin">Django Admin "manage.py"</a>

-[B] The outer mysite/ root directory is a container for your project.
    ~Its name doesn’t matter to Django; you can rename it to anything you like.

-[B./] The inner mysite/ directory is the actual Python package for your project.
    ~Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

-[B.1] mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. <a href="https://docs.python.org/3/tutorial/modules.html#tut-packages">Python Packages</a>

-[B.2] mysite/settings.py: Settings/configuration for this Django project.
    ~Django settings will tell you all about how settings work. <a href="https://docs.djangoproject.com/en/4.2/topics/settings">Site Settings</a>

-[B.3] mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
    ~You can read more about URLs in URL dispatcher. <a href="https://docs.djangoproject.com/en/4.2/topics/http/urls"> URLS </a>
    ~Example of


### ClosingNotes ###

~ProfileName.github.io
    -> is not able to able to run anything other that UI:[html,css,js]
    -> Though Django is an FreeToUse framework, (by the devs, for the devs)
    -> Hosting such a project on a cloud server will require Cloud Computing
        on a dedicated server and can cost anywhere from $40 to $100 +..
        if you do have the means to host locally, please be careful, as 
        Django is a very popular tool, and not only do multiple devs use it,
        but just as many are very capable of exploiting it, and can cause
        potential risks to you and/or anyone using your service.. 
        ..but if you're og, have at it, thanks for reading my blunders :P..

