from django.db import models
from django.contrib.auth.models import User


class ContactForm(models.Model):
    """
    Contact form model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    add_reason = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.owner} : {self.add_reason}"
