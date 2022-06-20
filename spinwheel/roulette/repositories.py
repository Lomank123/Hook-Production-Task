from roulette.models import Round, Spin


class RoundRepository:

    @staticmethod
    def get_not_deleted_or_create() -> Round:
        spin_round = Round.objects.filter(is_deleted=False).first()
        if spin_round is None:
            spin_round = Round.objects.create()
        return spin_round


class SpinRepository:
    pass
