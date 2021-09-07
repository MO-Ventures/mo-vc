from django.views.generic import ListView
from people.models import Employee, Sector
from typing import Any, Dict

# Create your views here.
class PeopleListView(ListView):
    template_name = 'people/index.html'
    model = Employee

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['sector'] = set([employee.sector for employee in Employee.objects.all()])
        context['navbar'] = 'text-black'
        context['people'] = Employee.objects.all().exclude(sector=Sector.Advisory_board)
        context['advisory_board'] = Employee.objects.filter(sector=Sector.Advisory_board)
        return context