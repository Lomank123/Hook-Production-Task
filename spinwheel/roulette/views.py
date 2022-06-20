from django.views.generic.base import TemplateView


class SpinWheelView(TemplateView):
    template_name = "roulette/spinwheel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StatsView(TemplateView):
    template_name = "roulette/stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
