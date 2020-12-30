from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.response import Response
from rest_framework import status

from Bugclaim.permissions import UserIsRootAdminOrReadOnly, UserIsRootModOrReadOnly, UserIsCompanyAdminOrReadOnly, \
    UserIsCompanyModOrReadOnly, UserIsResearcherOrReadOnly
from api.dashboard.users.serializers import RootModSerializer, CompanyAdminSerializer, CompanyModSerializer, \
    ResearcherSerializer
from users.models import User
from .serializers import RootAdminSerializer


class RootAdminView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = RootAdminSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsRootAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['username'] = instance.username
        request.data._mutable = mutable
        serializer = RootAdminSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

class RootModView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = RootModSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsRootModOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['username'] = instance.username
        request.data._mutable = mutable
        serializer = RootModSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

class CompanyAdminView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = CompanyAdminSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsCompanyAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['username'] = instance.username
        request.data._mutable = mutable
        serializer = CompanyAdminSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

class CompanyModView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = CompanyModSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsCompanyModOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        mutable = request.data._mutable
        request.data._mutable = True
        request.data['username'] = instance.username
        request.data._mutable = mutable
        serializer = CompanyModSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

class ResearcherView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = RootAdminSerializer
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
