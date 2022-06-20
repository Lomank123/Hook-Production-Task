import logging
from random import choice

from rest_framework import status
from rest_framework.response import Response
from spinwheel import consts

from roulette.repositories import RoundRepository, SpinRepository
from roulette.serializers import RoundSerializer, SpinSerializer


logger = logging.getLogger('django')


class SpinWheelService:

    def _perform_spin(self, spin_round):
        """
        Create new round if slots array is empty and return jackpot.
        Otherwise remove random value, return it and save round.
        """
        slots = spin_round.slots["slots"].copy()
        value = consts.JACKPOT_VALUE
        if len(slots) == 0:
            # Set current round as deleted
            spin_round.is_deleted = True
            logger.info("Jackpot!")
        else:
            # pop random value from slots
            index = choice(range(0, len(slots)))
            value = slots.pop(index)
            logger.info(f"Removed slot is: {value}")
            spin_round.slots["slots"] = slots
        RoundRepository.save(spin_round)
        return value

    def get_current_round_execute(self):
        spin_round = RoundRepository.get_not_deleted_or_create()
        serializer = RoundSerializer(spin_round)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def make_spin_execute(self, round_id, user_id):
        spin_round = RoundRepository.get_by_id(round_id)
        value = self._perform_spin(spin_round)
        # Save spin value
        SpinRepository.create(spin_round_id=round_id, user_id=user_id, value=value)
        return Response(data={"value": value}, status=200)


class StatsService:
    pass
