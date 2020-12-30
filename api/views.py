from rest_auth.views import LoginView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomLoginView(LoginView):
    def get_response(self):
        role = {'0': "root admin", '1': "root moderator", '2': "company admin", '3': "company moderator",
                '4': "researcher"}
        orginal_response = super().get_response()
        mydata = {"user role": "user is a " + role[self.request.user.user_type],
                  "user_type": self.request.user.user_type, "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response


class UserStatusView(generics.RetrieveAPIView):
    """View To Return The User Status (Active/Superuser)"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *Args, **kwargs):
        user_instance = request.user
        data = {'is_active': user_instance.is_active,
                'is_superuser': user_instance.is_superuser}
        return Response(data, status=status.HTTP_200_OK)
