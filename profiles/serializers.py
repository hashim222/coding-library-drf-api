from rest_framework import serializers
from .models import Profile
from followers.models import Follower


# Help was taken from Code Institute's DRF API walkthrough project.
class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer to converts Profile models into JSON,
    which can be used for frontend.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Checks if the requested user is the same as the owner.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        '''
        When a logged-in user follows another user, the following Id
        is displayed in the profile.
        If not logged in, it will display None.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            if following:
                return following.id
            else:
                return None
        else:
            return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'years_of_experience', 'favourite_programming_language',
            'about_me', 'image', 'is_owner', 'following_id'
        ]
