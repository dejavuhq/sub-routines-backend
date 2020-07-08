from django.conf import settings
from django.urls import include, path

from rest_framework.routers import DefaultRouter, SimpleRouter

from subroutines.users.views import UserViewSet
from subroutines.habits.views import HabitViewSet
from subroutines.stats.views import StatViewSet

router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet)
router.register("habits", HabitViewSet)
router.register("stats", StatViewSet)

app_name = "api"
urlpatterns = [
    path("api/", include(router.urls)),
]
