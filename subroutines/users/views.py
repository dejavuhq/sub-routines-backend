from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from subroutines.users.serializers import (
    UserSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
    ProfileModelSerializer,
)


User = get_user_model()


class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = "username"

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ["signup", "login"]:
            permissions = [AllowAny]
        elif self.action in ["retrieve", "update", "partial_update", "profile"]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    @action(detail=False, methods=["POST"])
    def signup(self, request):
        """Handle user sign up."""
        serializer = UserSignUpSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user, context={"request": request}).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"])
    def login(self, request):
        """Handle user login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserSerializer(user).data, "token": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["put", "patch"])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == "PATCH"
        serializer = ProfileModelSerializer(profile, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserSerializer(user).data
        return Response(data)
