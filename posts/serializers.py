from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bookmark_posts.models import Bookmark


# Help was taken from Code Institute's DRF API walkthrough project.
class PostSerializer(serializers.ModelSerializer):
    '''
    Post serializer to converts Post models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    bookmark_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        '''
        If a user posts an image larger than the given size,
        a warning message will be displayed.
        '''
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'You have uploaded an image larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "uploaded image's width is larger than 4096px!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "uploaded image's height is larger than 4096px!"
            )
        return value

    def get_is_owner(self, obj):
        '''
        Checks if the requested user is the same as the owner.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        '''
        When a logged-in user likes the post,
        the like Id will be displayed in the post.
        If not logged in, it will display None.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                post=obj
            ).first()
            if like:
                return like.id
            else:
                return None
        else:
            return None

    def get_bookmark_id(self, obj):
        '''
        When a logged-in user bookmarks the post,
        the bookmark Id will be displayed in the post.
        If not logged in, it will display None.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user,
                post=obj
            ).first()
            if bookmark:
                return bookmark.id
            else:
                return None
        else:
            return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'updated_on', 'title', 'caption',
            'image', 'like_id', 'bookmark_id', 'comments_count', 'likes_count',
            'bookmark_count'
        ]
