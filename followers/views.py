from rest_framework import generics, permissions
from coding_library.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# Help was taken from Code Institute's DRF API walkthrough project.
class FollowerList(generics.ListCreateAPIView):
    '''
    Users can follow other users and they will be displayed on the List.
    '''
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    '''
    Retrieves single user info by Id and the owner can unfollow
    the user he is following.
    '''
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
