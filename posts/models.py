from django.db import models
from django.contrib.auth.models import User


# Help was taken from Code Institute's DRF API walkthrough project.
# Updates were made.
class Post(models.Model):
    '''
    User's post model which is related to owner.
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_z0gbil', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id}: {self.title}'
