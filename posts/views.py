from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
from coding_library.permissions import IsOwnerOrReadOnly


# Help was taken from Code Institute's DRF API walkthrough project.
class PostList(generics.ListCreateAPIView):
    '''
    Posts can be created and displayed.
    '''
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Posts can be retrieved, updated, and deleted.
    '''
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
