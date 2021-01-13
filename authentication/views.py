from rest_auth.views import LoginView
from rest_framework.response import Response
from users.models import Roles,User
from authentication.exceptions import AuthenticationError
from rest_framework_simplejwt.tokens import RefreshToken
from abc import ABC, abstractmethod




class LoginBaseClass(ABC,LoginView):
    '''
    This class inherits the LoginView from the rest_auth
    package. Rest auth does not support the refresh token 
    logic. However,restframework_simplejwt does. Rest auth was
    used because its based off all-auth which can be used for
    social logins as well as signing in with either username or 
    password(of which simlejwt does not support). The two libraries
    were combined to give the required results
    '''

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    @abstractmethod
    def login(self):
        pass

    def get_response(self):
        data = {}
        
        refresh = self.get_token(self.user)
        # generate access and refresh tokens 
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return Response(data)

    









class StaffLoginView(LoginBaseClass):

    def login(self):
        try:
            self.user = self.serializer.validated_data['user']
            # check if user has practitioner among its roles
            self.user.role.get(display='staff')
            return self.user
        except Roles.DoesNotExist:
            raise AuthenticationError
            








class PatientLoginView(LoginBaseClass):

    def login(self):
        try:
            self.user = self.serializer.validated_data['user']
            # check if user has patient among its roles
            self.user.role.get(id='patient')
            return self.user
        except Roles.DoesNotExist:
            raise AuthenticationError









class AdminLoginView(LoginBaseClass):

    def login(self):
        try:
            self.user = self.serializer.validated_data['user']
            # check if user is a corporate admin
            self.user.role.get(display='admin')
            return self.user
        except Roles.DoesNotExist:
            raise AuthenticationError







class SupportLoginView(LoginBaseClass):

    def login(self):
        try:
            self.user = self.serializer.validated_data['user']
            self.user.role.get(display='support')
            return self.user
        except Roles.DoesNotExist:
            raise AuthenticationError



