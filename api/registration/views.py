from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_auth.registration.views import RegisterView

from Bugclaim.permissions import IsRootAdmin, IsCompanyAdmin, IsRootModOrAdmin


class AdminModeratorRegisterView(RegisterView):
    permission_classes = (IsAuthenticated, IsRootAdmin)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '1'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class AdminRegisterView(RegisterView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, IsAdminUser)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '0'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class CompanyModeratorRegisterView(RegisterView):
    permission_classes = (IsAuthenticated, IsCompanyAdmin)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '3'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class CompanyRegisterView(RegisterView):
    permission_classes = (IsAuthenticated, IsRootModOrAdmin)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '2'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response


class ResearcherRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '4'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response
