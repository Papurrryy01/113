from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #class-based view
    template_name = 'pages/home.html' #Link our view to the html


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
