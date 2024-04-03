from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            logger.error("Email or password not provided.")
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            logger.info(f"User {email} authenticated successfully.")
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        else:
            logger.error(f"Authentication failed for user {email}.")
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)