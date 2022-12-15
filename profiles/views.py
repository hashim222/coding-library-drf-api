from rest_framework import generics, filters
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from coding_library.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Display all the user's profile.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed__created_on'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Each profile can be retrieved by ID and updated as well.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')
