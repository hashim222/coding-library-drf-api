from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer converts Django models into JSON, 
    which can be used for a frontend.
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'favourite_programming_language', 'about_me', 'image'
        ]
