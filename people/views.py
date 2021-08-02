from django.views.generic import ListView
from people.models import Introduction, People
from typing import Any, Dict

# Create your views here.
class PeopleListView(ListView):
    template_name = 'people/index.html'
    model = People

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['sector'] = set([people.sector for people in People.objects.all()])
        context['navbar'] = 'text-black'
        context['intro'] = Introduction.objects.first()
        return context