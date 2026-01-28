from django.urls import path

from .views import (
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    SignUpView,
)

# Create your views here.


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
