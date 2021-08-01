from django.views.generic import ListView
from django.utils.translation import gettext as _
from portfolio.models import Company, Sector, Statistics
from typing import Any, Dict, List

# Create your views here.
class CompanyListView(ListView):
    template_name = 'portfolio/index.html'
    model = Company

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['stat'] = Statistics.objects.first
        context['investment'] = [
        # Integrity, 
            {
                "name": _("Transparency"),
                "description": _("We value")
            },
            {
                "name": _("Founder"),
                "description": _("We value")
            },
            {
                "name": _("Responsiblity"),
                "description": _("We value")
            },
            {
                "name": _("Sustainable"),
                "description": _("We value")
            },
            {
                "name": _("Profitable"),
                "description": _("We value")
            },
        ]
        return context