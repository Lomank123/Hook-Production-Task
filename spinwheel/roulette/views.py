from django.views.generic.base import TemplateView

from roulette.services import SpinWheelService, StatsService


class SpinWheelView(TemplateView):
    template_name = "roulette/spinwheel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_context = SpinWheelService().execute()
        context.update(service_context)
        return context


class StatsView(TemplateView):
    template_name = "roulette/stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_context = StatsService().execute()
        context.update(service_context)
        return context
