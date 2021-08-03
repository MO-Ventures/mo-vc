from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from philosophy.models import Philosophy
from typing import Any, Dict

# Create your views here.
class PhilosophyListView(ListView):
    template_name = 'philosophy/index.html'
    model = Philosophy

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        context['list'] = ', '.join(f'"{w.name}"' for w in Philosophy.objects.all())
        return context