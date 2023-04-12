from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


# Create your models here.
class PostDash(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    color       = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    def __str__(self):
        return str(self.title) + " | " + str(self.author)


    def get_absolute_url(self):
        print("[RETURNING DASHBOARDS]")
        return reverse('dashboards')


