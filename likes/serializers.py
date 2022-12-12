from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


# Help was taken from Code Institute's DRF API walkthrough project.
class LikeSerializer(serializers.ModelSerializer):
    '''
    Like serializer to converts Like models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'created_on']

    def create(self, validated_data):
        '''
        If a user likes the same post multiple times,
        it will throw a duplicate error.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
