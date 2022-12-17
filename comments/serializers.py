from django.contrib.humanize.templatetags.humanize import naturaltime
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
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Checks if the requested user is the same as the owner.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        '''
        Displays when the comments were created.
        '''
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        '''
        Displays when the comments were updated.
        '''
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'post',
            'created_on', 'updated_on', 'comment'
        ]


class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for the Comment model used in Detail view.
    CommentDetailSerializer inherits from CommentSerializer,
    all its methods and attributes.
    '''
    post = serializers.ReadOnlyField(source='post.id')
