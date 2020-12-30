from rest_framework import serializers

from users.models import User


class UserStatus(serializers.ModelSerializer):
    """DRF Serializer To Get The Status Of The User (Active/Superuser)"""

    class Meta:
        model = User
        fields = ['is_active', 'is_superuser']