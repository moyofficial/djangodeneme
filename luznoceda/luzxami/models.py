from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):



    title = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=50, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=1000)

    date_created = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

def __str__(self):

    return "self.title[:20]"