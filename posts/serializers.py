from rest_framework import serializers
from .models import Post


# Help was taken from Code Institute's DRF API walkthrough project.
class PostSerializer(serializers.ModelSerializer):
    '''
    Profile serializer to converts Django models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

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

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'updated_on', 'title', 'caption', 'image'
        ]
