from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #class-based view
    template_name = 'pages/home.html' #Link our view to the html


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return redirect("home")
