from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Help was taken from Code Institute's DRF API walkthrough project.
class Comment(models.Model):
    '''
    Comment model, which is related to User and Post.
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment
