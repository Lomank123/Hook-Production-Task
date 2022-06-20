from roulette.models import Round, Spin


class RoundRepository:

    @staticmethod
    def get_not_deleted_or_create():
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
