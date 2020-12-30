from rest_framework import serializers

from django.contrib.auth import get_user_model

from root.models import RootAdmin, Rootmod

User = get_user_model()

class RootAdminSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='rootadmin.bio', allow_blank=True, allow_null=True)
    country = serializers.CharField(
        source='rootadmin.country', allow_blank=True, allow_null=True)
    facebook_url = serializers.URLField(
        source='rootadmin.facebook_url', allow_blank=True, allow_null=True)
    twitter_handler = serializers.CharField(
        source='rootadmin.twitter_handler', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio', 'country', 'facebook_url', 'twitter_handler']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('rootadmin', None)
        print("hllo")
        self.update_or_create_profile(instance, profile_data)
        return super(RootAdminSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        RootAdmin.objects.update_or_create(user=user, defaults=profile_data)


class RootModSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='rootmod.bio', allow_blank=True, allow_null=True)
    country = serializers.CharField(
        source='rootmod.country', allow_blank=True, allow_null=True)
    facebook_url = serializers.URLField(
        source='rootmod.facebook_url', allow_blank=True, allow_null=True)
    twitter_handler = serializers.CharField(
        source='rootmod.twitter_handler', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio', 'country', 'facebook_url', 'twitter_handler']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('rootmod', None)
        self.update_or_create_profile(instance, profile_data)
        return super(RootModSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        Rootmod.objects.update_or_create(user=user, defaults=profile_data)

