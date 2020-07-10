from django.urls import include, path

from rest_framework.routers import DefaultRouter

from subroutines.habits.views import HabitViewSet, InstanceViewSet

router = DefaultRouter(trailing_slash=False)
router.register("habits", HabitViewSet, basename="habits")
router.register("instances", InstanceViewSet, basename="instances")

urlpatterns = [
    path("", include(router.urls)),
]
