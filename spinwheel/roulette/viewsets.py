from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from roulette import serializers
from roulette.models import Round, Spin
from roulette.services import SpinWheelService, StatsService


# TODO: Replace ModelViewSet with APIView
class RoundViewSet(ModelViewSet):
    serializer_class = serializers.RoundSerializer

    def get_queryset(self):
        return Round.objects.all()

    @action(methods=["get"], detail=False)
    def get_current_round(self, request):
        return SpinWheelService().get_current_round_execute()

    @action(methods=["post"], detail=False)
    def make_spin(self, request):
        return SpinWheelService().make_spin_execute(request.data["round_id"], request.user.id)


class SpinViewSet(ModelViewSet):
    serializer_class = serializers.SpinSerializer

    def get_queryset(self):
        return Spin.objects.all()
