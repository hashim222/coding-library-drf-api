from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    '''
    Follower serializer to converts Follower models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_on', 'followed', 'followed_name'
        ]

    # Help was taken from Code Institute's DRF API walkthrough project.
    def create(self, validated_data):
        '''
        If a user tries to follow the same user multiple times,
        it will throw a duplicate error.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
