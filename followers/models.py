from django.db import models
from django.contrib.auth.models import User


# Help was taken from Code Institute's DRF API walkthrough project.
class Follower(models.Model):
    '''
    Follower model.
    Users can follow each other.
    '''
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'Owner: {self.owner} - Followed User: {self.followed}'
