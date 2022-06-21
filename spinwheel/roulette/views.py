from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class SpinWheelView(TemplateView):
    template_name = "roulette/spinwheel.html"


class CustomLoginView(LoginView):
    template_name = 'roulette/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'roulette/logout.html'
    next_page = '/'
