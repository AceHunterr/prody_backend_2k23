from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
