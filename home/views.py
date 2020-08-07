from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def show_chart(request):
    return render(request, 'home_base.html')

class AboutPageView(TemplateView):
    template_name='about.html'
