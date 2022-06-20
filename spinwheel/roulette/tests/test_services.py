from django.test import TestCase
from roulette.services import SpinWheelService, StatsService
from roulette.models import Spin, Round
from django.contrib.auth.models import User

from spinwheel import consts


class SpinWheelServiceTestCase(TestCase):

    def setUp(self):
        self.round1 = Round.objects.create()
        self.round2 = Round.objects.create(slots={"slots": []}, is_deleted=True)
        self.user1 = User.objects.create(username="test1", password="123123123Aa")

    def tearDown(self):
        self.round1.delete()
        self.round2.delete()
        self.user1.delete()

    def test_get_current_round_execute(self):
        self.assertEqual(Round.objects.count(), 2)
        # Get
        response = SpinWheelService().get_current_round_execute()
        self.assertEqual(response.data["id"], 1)
        self.round1.is_deleted = True
        self.round1.save()
        # Create
        response = SpinWheelService().get_current_round_execute()
        self.assertEqual(Round.objects.count(), 3)
        self.assertEqual(response.data["id"], 3)

    def test_make_spin_execute(self):
        self.assertEqual(Round.objects.count(), 2)
        response = SpinWheelService().make_spin_execute(self.round1.id, self.user1.id)
        self.assertTrue("value" in response.data.keys())
        self.assertTrue(response.data["value"] in range(1, 11))
        self.assertEqual(Spin.objects.count(), 1)
        # 2nd case where we get jackpot
        new_round = Round.objects.create(slots={"slots": []})
        self.assertEqual(Round.objects.count(), 3)
        response = SpinWheelService().make_spin_execute(new_round.id, self.user1.id)
        self.assertEqual(response.data["value"], consts.JACKPOT_VALUE)
        self.assertEqual(Spin.objects.count(), 2)
        new_round = Round.objects.get(id=new_round.id)
        self.assertTrue(new_round.is_deleted)


class StatsServiceTestCase(TestCase):
    pass
