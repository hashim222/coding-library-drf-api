from rest_framework import generics, permissions
from coding_library.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


# Help was taken from Code Institute's DRF API walkthrough project.
class LikeList(generics.ListCreateAPIView):
    '''
    Post can be liked and viewed by users.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Likes can be retrieved and deleted.
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
