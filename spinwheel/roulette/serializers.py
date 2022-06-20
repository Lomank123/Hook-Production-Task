from rest_framework import serializers

from roulette import models


class RoundSerializer(serializers.ModelSerializer):
    slots = serializers.JSONField(initial=models.round_jsonfield_default)

    class Meta:
        fields = "__all__"
        model = models.Round


class SpinSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = models.Spin
