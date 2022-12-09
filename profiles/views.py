from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from coding_library.permissions import IsOwnerOrReadOnly


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
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
