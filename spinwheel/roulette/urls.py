from django.urls import path, include
from rest_framework.routers import DefaultRouter
from roulette import viewsets
from roulette import views


router = DefaultRouter()
router.register("round", viewsets.RoundViewSet, basename="round")
router.register("spin", viewsets.SpinViewSet, basename="spin")


urlpatterns = [
    path("", views.SpinWheelView.as_view(), name="spinwheel"),
    path("stats/", views.StatsView.as_view(), name="stats"),
    path("api/", include(router.urls)),
]
