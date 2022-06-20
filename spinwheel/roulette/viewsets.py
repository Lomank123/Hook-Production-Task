from rest_framework.viewsets import ModelViewSet
from roulette import serializers
from roulette.models import Round, Spin


class RoundViewSet(ModelViewSet):
    serializer_class = serializers.RoundSerializer

    def get_queryset(self):
        return Round.objects.all()


class SpinViewSet(ModelViewSet):
    serializer_class = serializers.SpinSerializer

    def get_queryset(self):
        return Spin.objects.all()
