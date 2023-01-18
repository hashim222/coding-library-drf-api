from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact Form model

    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        """
        Returns a human readable time since the
        user message was created
        eg. '2 days ago'
        """
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        """
        Returns a human readable time since the
        user message was updated
        eg. '15 minutes ago'
        """
        return naturaltime(obj.updated_on)

    class Meta:
        """
        Lists all the filds to be included in
        the data returned by this api
        """
        model = ContactForm
        fields = [
            "id",
            "owner",
            "add_reason",
            "message",
            "profile_id",
            "profile_image",
            "created_on",
            "updated_on",
        ]
