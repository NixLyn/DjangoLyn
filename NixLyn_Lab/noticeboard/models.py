from django.db import models

# New Posts For the NoticeBoard
class New_Posts(models.Model):
    author_postn    = models.CharField(max_length=600)
    new_post_title  = models.CharField(max_length=200)
    new_post_sum    = models.CharField(max_length=600)
    pub_date        = models.DateTimeField("date published")
    def __str__(self):
        return str(self.author_postn) + " | " + str(self.new_post_title)+ " | " + str(self.new_post_sum)

# Responses on each New_Post
class Choice(models.Model):
    author_respn    = models.CharField(max_length=600)
    question        = models.ForeignKey(New_Posts, on_delete=models.CASCADE)
    response_text   = models.CharField(max_length=500)
    votes           = models.IntegerField(default=0)
    def __str__(self):
        return str(self.author_respn) + " | " + str(self.question)

