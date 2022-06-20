from django.views.generic.base import TemplateView


class SpinWheelView(TemplateView):
    template_name = "roulette/spinwheel.html"


class StatsView(TemplateView):
    template_name = "roulette/stats.html"
