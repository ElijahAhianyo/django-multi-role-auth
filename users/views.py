from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer




class UserDetailListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        user_list = User.objects.all()
        serializer = UserSerializer(user_list,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
