from django.conf import settings
from django.urls import include, path

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from subroutines.users.views import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
    path("api/", include(router.urls)),
]
