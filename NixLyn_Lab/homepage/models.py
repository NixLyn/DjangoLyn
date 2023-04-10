from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    color   = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    body = models.TextField()
    add_on = models.CharField(max_length=50, default="SideNote: ")
    date_made  = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.title) + " | " + str(self.author)


    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))
