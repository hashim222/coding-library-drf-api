from rest_framework import serializers
from .models import Profile


# Help was taken from Code Institute's DRF API walkthrough project.
class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer to converts Profile models into JSON,
    which can be used for frontend.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Checks if the requested user is the same as the owner.
        '''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'years_of_experience', 'favourite_programming_language',
            'about_me', 'image', 'is_owner',
        ]
