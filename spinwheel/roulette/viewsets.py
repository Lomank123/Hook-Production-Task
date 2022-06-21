from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from roulette import serializers
from roulette.services import SpinWheelService, StatsService


class SpinWheelViewSet(ViewSet):
    serializer_class = serializers.RoundSerializer

    @action(methods=["get"], detail=False)
    def get_current_round(self, request):
        return SpinWheelService().get_current_round_execute()

    @action(methods=["post"], detail=False)
    def make_spin(self, request):
        return SpinWheelService().make_spin_execute(request.data["round_id"], request.user.id)

    @action(methods=["get"], detail=False)
    def get_stats(self, request):
        return StatsService().get_stats_execute()
