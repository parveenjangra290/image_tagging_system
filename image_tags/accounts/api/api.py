"""
    Serializer Login.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.api.serializers import (UserLoginSerializer, UserProfileSerializer)


class UserAPIViewSet(viewsets.GenericViewSet):
    """
    User login API.
    """

    @action(detail=False, methods=['POST'], serializer_class=UserLoginSerializer, permission_classes=[AllowAny])
    def login(self, request):
        """
            Login method verify request login details.
            :param request:
            :return Response:
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = serializer.login()
            return Response(UserProfileSerializer(instance=result).data, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
