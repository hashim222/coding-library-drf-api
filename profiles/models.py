from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Help was taken from Code Institute's DRF API walkthrough project.
# Updates were made.
class Profile(models.Model):
    """
    Users's Profile Model
    """
    PROGRAMMING_LANGUAGE = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Javascript', 'Javascript'),
        ('python', 'python'),
        ('Java', 'Java'),
        ('C and C++', 'C and C++'),
        ('PHP', 'PHP'),
        ('C#', 'C#'),
    ]
    YEARS = [
        ('Less than 1 year', 'Less than 1 year'),
        ('1 Year', '1 Year'),
        ('2 Years', '2 Years'),
        ('3 Years', '3 Years'),
        ('4 Years', '4 Years'),
        ('5 or More years', '5 or More years')
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    years_of_experience = models.CharField(
        max_length=50, choices=YEARS, blank=True)
    favourite_programming_language = models.CharField(
        max_length=20, choices=PROGRAMMING_LANGUAGE, blank=True)
    about_me = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_sgymh1')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Creates a profile whenever a new user is created"""
    if created:
        Profile.objects.create(owner=instance)
