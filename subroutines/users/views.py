from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from subroutines.users.models import User
from subroutines.users.serializers import (
    UserSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
    AccountVerificationSerializer,
)


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = "username"

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ["signup", "login", "verify"]:
            permissions = [AllowAny]
        elif self.action in ["retrieve", "update", "partial_update"]:
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

        data = {
            "user": UserSerializer(user).data,
            "token": str(token.access_token),
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"message": "Congratulations! Start making habits."}
        return Response(data, status=status.HTTP_200_OK)

