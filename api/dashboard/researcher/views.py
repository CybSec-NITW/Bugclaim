from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from Bugclaim.permissions import UserIsResearcherOrReadOnly
from api.dashboard.researcher.serializers import ResearcherSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ResearcherView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = ResearcherSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsResearcherOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['username'] = instance.username
        request.data._mutable = mutable
        serializer = ResearcherSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.data)
        return Response(serializer.data)


class UserStatusView(generics.RetrieveAPIView):
    """View To Return The User Status (Active/Superuser)"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *Args, **kwargs):
        user_instance = request.user
        data = {'is_active': user_instance.is_active,
                'is_superuser': user_instance.is_superuser}
        return Response(data, status=status.HTTP_200_OK)
