import os
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        context["kakao_api_key"] = os.environ.get('KAKAO_API_KEY', None)
        return context
    