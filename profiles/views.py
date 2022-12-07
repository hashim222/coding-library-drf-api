from rest_framework import generics
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Display all the user's profile.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Each profile can be retrieved by ID and updated as well.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
