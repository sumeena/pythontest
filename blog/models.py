from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    POST = 1
    NEWS = 2

    ENTRY_TYPES = (
        (POST, 'Post'),
        (NEWS, 'News')
    )

    user = models.ForeignKey(User)
    entry_type = models.IntegerField(default=POST, choices=ENTRY_TYPES)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
