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
