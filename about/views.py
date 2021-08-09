from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from typing import Any, Dict

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context