from django.urls import path

from people.views import PeopleListView

urlpatterns = [
    path('', PeopleListView.as_view()),
]