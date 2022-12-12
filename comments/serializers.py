from rest_framework import serializers
from .models import Comment


# Help was taken from Code Institute's DRF API walkthrough project.
class CommentSerializer(serializers.ModelSerializer):
    '''
    Comment serializer to converts Comment models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''
        Checks if the requested user is the same as the owner.
        '''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'post',
            'created_on', 'updated_on', 'comment'
        ]


class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for the comment model used in Detail view.
    CommentDetailSerializer inherits from CommentSerializer,
    all its methods and attributes.
    '''
    post = serializers.ReadOnlyField(source='post.id')
