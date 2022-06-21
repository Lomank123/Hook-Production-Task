from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from roulette.forms import CustomUserCreationForm


class SpinWheelView(LoginRequiredMixin, TemplateView):
    template_name = "roulette/spinwheel.html"


class CustomLoginView(LoginView):
    template_name = 'roulette/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'roulette/logout.html'
    next_page = '/'


class CustomSignupView(CreateView):
    model = get_user_model()
    template_name = 'roulette/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(CustomSignupView, self).form_valid(form)
        raw_password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return valid
