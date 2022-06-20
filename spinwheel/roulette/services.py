from rest_framework import status
from rest_framework.response import Response

from roulette.repositories import RoundRepository, SpinRepository
from roulette.serializers import RoundSerializer, SpinSerializer


class SpinWheelService:

    def _build_context(self):
        spin_round = RoundRepository.get_not_deleted_or_create()
        return {
            "round": spin_round,
        }

    def execute(self):
        context = self._build_context()
        return context

    def get_current_round_execute(self):
        spin_round = RoundRepository.get_not_deleted_or_create()
        serializer = RoundSerializer(spin_round)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class StatsService:

    def _build_context(self):
        return {
            "data": 1,
        }

    def execute(self):
        context = self._build_context()
        return context
