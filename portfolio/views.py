from django.views.generic import ListView
from django.utils.translation import gettext as _
from portfolio.models import Company, Region, Statistics
from typing import Any, Dict, List

# Create your views here.
class CompanyListView(ListView):
    template_name = 'portfolio/index.html'
    model = Company

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['stat'] = Statistics.objects.first
        return context