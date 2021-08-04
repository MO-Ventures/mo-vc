from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from typing import Any, Dict

# Create your views here.
class BusinessModelView(TemplateView):
    template_name = 'about/business_model.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context
    

class PhilosophyView(TemplateView):
    template_name = 'about/philosophy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context