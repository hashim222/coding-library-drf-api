from rest_framework import generics, permissions
from .serializers import CommentSerializer, CommentDetailSerializer
from .models import Comment
from coding_library.permissions import IsOwnerOrReadOnly


# Help was taken from Code Institute's DRF API walkthrough project.
class CommentList(generics.ListCreateAPIView):
    '''
    Comments are created and displayed.
    '''
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Comments can be retrieved, updated, and deleted.
    '''
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
