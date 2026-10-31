from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

from .serializers import LoginSerializer


# Create your views here.
# --------------------------------
# API Login / Swagger Login
# --------------------------------


class LoginApiView(APIView):

    @swagger_auto_schema(
    request_body=LoginSerializer
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'username': user.username,
                'role': user.role,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        
        return Response(serializer.errors, status=400)