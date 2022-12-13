from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    '''
    Bookmark serializer to converts Bookmark models into JSON,
    which can be used for frontend.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'post', 'created_on']

    # Help was taken from Code Institute's DRF API walkthrough project.
    def create(self, validated_data):
        '''
        If a user tries to Bookmark the same post multiple times,
        it will throw a duplicate error.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
