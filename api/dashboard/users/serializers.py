from rest_framework import serializers

from users.models import RootAdmin, Researcher, Rootmod, CompanyAdmin, CompanyMod

from users.models import User


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


class CompanyAdminSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='companyadmin.bio', allow_blank=True, allow_null=True)
    country = serializers.CharField(
        source='companyadmin.country', allow_blank=True, allow_null=True)
    facebook_url = serializers.URLField(
        source='companyadmin.facebook_url', allow_blank=True, allow_null=True)
    twitter_handler = serializers.CharField(
        source='companyadmin.twitter_handler', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio', 'country', 'facebook_url', 'twitter_handler']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('companyadmin', None)
        self.update_or_create_profile(instance, profile_data)
        return super(CompanyAdminSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        CompanyAdmin.objects.update_or_create(user=user, defaults=profile_data)


class CompanyModSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='companymod.bio', allow_blank=True, allow_null=True)
    country = serializers.CharField(
        source='companymod.country', allow_blank=True, allow_null=True)
    facebook_url = serializers.URLField(
        source='companymod.facebook_url', allow_blank=True, allow_null=True)
    twitter_handler = serializers.CharField(
        source='companymod.twitter_handler', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio', 'country', 'facebook_url', 'twitter_handler']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('companymod', None)
        self.update_or_create_profile(instance, profile_data)
        return super(CompanyModSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        CompanyMod.objects.update_or_create(user=user, defaults=profile_data)


class ResearcherSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='profile.bio', allow_blank=True, allow_null=True)
    country = serializers.CharField(
        source='profile.country', allow_blank=True, allow_null=True)
    facebook_url = serializers.URLField(
        source='profile.facebook_url', allow_blank=True, allow_null=True)
    twitter_handler = serializers.CharField(
        source='profile.twitter_handler', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio', 'country', 'facebook_url', 'twitter_handler']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""
        profile_data = validated_data.pop('profile', None)
        self.update_or_create_profile(instance, profile_data)
        return super(ResearcherSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        Researcher.objects.update_or_create(user=user, defaults=profile_data)


class UserStatus(serializers.ModelSerializer):
    """DRF Serializer To Get The Status Of The User (Active/Superuser)"""

    class Meta:
        model = User
        fields = ['is_active', 'is_superuser']
