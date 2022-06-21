from django.db.models import Count, Subquery, OuterRef
from roulette.models import Round, Spin


class RoundRepository:

    @staticmethod
    def get_not_deleted_or_create():
        """
        Return first non-deleted Round or create new one.
        """
        spin_round = Round.objects.filter(is_deleted=False).first()
        if spin_round is None:
            spin_round = Round.objects.create()
        return spin_round

    @staticmethod
    def get_by_id(round_id):
        return Round.objects.get(id=round_id)

    @staticmethod
    def save(spin_round):
        return spin_round.save()


class SpinRepository:

    @staticmethod
    def create(*args, **kwargs):
        return Spin.objects.create(*args, **kwargs)

    @staticmethod
    def get_user_count_per_round():
        """
        Return list of {spin_round_id: user_count} for each round.
        """
        return list(
            Spin.objects
            .values("spin_round_id")
            .annotate(user_count=Count("user_id", distinct=True))
        )

    @staticmethod
    def get_active_users():
        """
        Return user id, round count and avg spins count.
        """
        user_spins_per_round = (
            Spin.objects
            .filter(spin_round_id=OuterRef("spin_round_id"), user_id=OuterRef("user_id"))
            .values("user_id")
            .annotate(count=Count("id"))
            .values("count")[:1]
        )
        round_count = Count("spin_round_id", distinct=True)
        data = list(
            Spin.objects
            .values("user_id")
            .annotate(round_count=round_count)
            .annotate(avg_spins_count=Count(Subquery(user_spins_per_round)) / round_count)
        )
        return data
