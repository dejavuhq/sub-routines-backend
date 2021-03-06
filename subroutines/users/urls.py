from django.urls import include, path

from rest_framework.routers import DefaultRouter

from subroutines.users.views import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
