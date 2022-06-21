from django.urls import include, path
from rest_framework.routers import DefaultRouter

from roulette import views, viewsets


router = DefaultRouter()
router.register("spinwheel", viewsets.SpinWheelViewSet, basename="spinwheel")


urlpatterns = [
    path("", views.SpinWheelView.as_view(), name="spinwheel"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("api/", include(router.urls)),
]
