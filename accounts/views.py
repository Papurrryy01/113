from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'

    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class StablePasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{user.password}{timestamp}"


class CustomPasswordResetView(PasswordResetView):
    token_generator = StablePasswordResetTokenGenerator()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    token_generator = StablePasswordResetTokenGenerator()
