import os
from django.shortcuts import render
from django.views.generic import TemplateView
from movc.settings import SECRETS

# Create your views here.
class ContactView(TemplateView):
    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        context["kakao_api_key"] = SECRETS['KAKAO_API_KEY']
        return context
    