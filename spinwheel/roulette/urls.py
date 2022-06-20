from django.urls import path, include
from rest_framework.routers import DefaultRouter
from roulette import viewsets


router = DefaultRouter()
router.register("round", viewsets.RoundViewSet, basename="round")
router.register("spin", viewsets.SpinViewSet, basename="spin")


urlpatterns = [
    path("api/", include(router.urls)),
]
