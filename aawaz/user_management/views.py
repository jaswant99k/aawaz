from django.shortcuts import get_object_or_404, render
from requests import request
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import UserProfile
from .serializers import UpdateUserProfile, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView




# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get(self, request):
        user = self.get_object(username = self.request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # def get(self):
    #     user = User.objects.filter(username=self.request.user)
    #     print(user)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

class UserListAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class ProfileUpdateAPIView(generics.UpdateAPIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = UpdateUserProfile
    lookup_field = 'user__username'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TestCallBackURL(APIView):
    def get(self, request):
        print(1)

#CALLBACK_URL_YOU_SET_ON_GOOGLE="http://localhost:8000//"
class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/"
    client_class = OAuth2Client
