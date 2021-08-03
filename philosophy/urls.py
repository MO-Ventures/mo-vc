from django.urls import path
from philosophy.views import PhilosophyListView

urlpatterns = [
    path('', PhilosophyListView.as_view()),
]