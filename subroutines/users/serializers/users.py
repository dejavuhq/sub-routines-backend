from django.contrib.auth import get_user_model, password_validation, authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from subroutines.users.models.profiles import Profile
from subroutines.users.serializers.profiles import ProfileModelSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_verified",
            "profile",
        ]


class UserSignUpSerializer(serializers.Serializer):
    """Handle user sign up data validation and user/profile creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Validate if passwords match."""
        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords don't match")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop("password_confirmation")
        user = User.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    """Handle user login data."""

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Validate credentials."""
        user = authenticate(username=data["username"], password=data["password"])

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        self.context["user"] = user
        return data

    def create(self, data):
        """Generate token."""
        token = RefreshToken.for_user(user=self.context["user"])
        return self.context["user"], token
