from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class MyCustomRegistrationSerializer(RegisterSerializer):
    ROOTADMIN = '0'
    ROOTMOD = '1'
    COMPANYADMIN = '2'
    COMPANYMOD = '3'
    RESEARCHER = '4'
    USER_TYPE_CHOICES = (
        (ROOTADMIN, "Root Admin"),
        (ROOTMOD, "Root Moderator"),
        (COMPANYADMIN, "Company Admin"),
        (COMPANYMOD, "Company Moderator"),
        (RESEARCHER, "RESEARCHER"),
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_type'] = self.validated_data.get('user_type', '')
        return data_dict