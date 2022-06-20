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


class StatsService:

    def _build_context(self):
        return {
            "data": 1,
        }

    def execute(self):
        context = self._build_context()
        return context
