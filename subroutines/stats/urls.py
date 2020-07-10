from django.urls import include, path

from rest_framework.routers import DefaultRouter

from subroutines.stats.views import StatViewSet

router = DefaultRouter(trailing_slash=False)
router.register("stats", StatViewSet, basename="stats")

urlpatterns = [
    path("", include(router.urls)),
]
