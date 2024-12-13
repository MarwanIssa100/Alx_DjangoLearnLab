from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserLoginSerializer , TokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

# User Registration View
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        login_serializer = UserLoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = login_serializer.validated_data['username']  # User object returned by validate
            token, _ = Token.objects.get_or_create(user=user)

            # Serialize the token with the custom serializer
            token_serializer = TokenSerializer(token)
            return Response(token_serializer.data, status=status.HTTP_200_OK)

        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
