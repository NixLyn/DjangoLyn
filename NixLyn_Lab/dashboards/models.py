from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    ('purple','PURPLE'),
    ('white','WHITE'),
)



# Create your models here.
class PostDash(models.Model):
    author      = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    color       = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    def __str__(self):
        return  str(self.author)  + " | " + str(self.color)


    def get_absolute_url(self):
        print("[RETURNING DASHBOARDS]")
        return reverse('dashboards')




class MyTarget(models.Model):
    author      = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mytarget       = models.CharField(max_length=150, null=True, default='url')
    def __str__(self):
        return  str(self.author)  + " | " + str(self.mytarget)



# ToDo:
# ? Create model for target profile [url/ip, recon_data{OS, ports,etc}, site_clone, heaps, report]
# ? Make admins able to edit the data, but not users...
