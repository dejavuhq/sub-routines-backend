from django.conf import settings
from django.urls import include, path

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from subroutines.users.views import UserViewSet
from subroutines.habits.views import HabitViewSet

router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet)
router.register("habits", HabitViewSet)
router.register("habits/<int:pk>", HabitViewSet, HabitViewSet.habit_detail)

app_name = "api"
urlpatterns = [
    path("api/", include(router.urls)),
]
