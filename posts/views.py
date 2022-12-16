from rest_framework import generics, permissions, filters
from django.db.models import Count
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
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        bookmark_count=Count('bookmark_posts', distinct=True)
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
        'bookmark_count',
        'likes__created_on',
        'bookmark_posts__created_on'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Posts can be retrieved, updated, and deleted.
    '''
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        bookmark_count=Count('bookmark_posts', distinct=True)
    ).order_by('-created_on')
