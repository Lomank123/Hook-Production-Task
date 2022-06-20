from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from spinwheel import consts


user_model = get_user_model()


def round_jsonfield_default():
    return {consts.SLOTS_NAME: list(range(1, 11))}


class Round(models.Model):
    """
    Represents spinwheel round. Has remained slots and participants.
    """

    slots = models.JSONField(default=round_jsonfield_default, verbose_name=_("Remained slots"))
    participants = models.ManyToManyField(
        user_model,
        blank=True,
        related_name="participants",
        verbose_name=_("Participants")
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Round")
        verbose_name_plural = _("Rounds")


class Spin(models.Model):
    """
    Single spin. Has user who spinned, value and round.
    """

    user = models.ForeignKey(user_model, on_delete=models.RESTRICT, verbose_name=_("User"))
    spin_round = models.ForeignKey(Round, on_delete=models.RESTRICT, verbose_name=_("Round"))
    value = models.IntegerField(verbose_name=_("Value"))

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Spin")
        verbose_name_plural = _("Spins")
