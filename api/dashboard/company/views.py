from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Bugclaim.permissions import UserIsCompanyAdminOrReadOnly, UserIsCompanyModOrReadOnly
from api.dashboard.company.serializers import CompanyAdminSerializer, CompanyModSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


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
