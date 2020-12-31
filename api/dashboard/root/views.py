from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Bugclaim.permissions import UserIsRootAdminOrReadOnly, UserIsRootModOrReadOnly
from api.dashboard.root.serializers import RootModSerializer
from .serializers import RootAdminSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RootAdminView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = RootAdminSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsRootAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
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
