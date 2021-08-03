from django.urls import path
from about.views import PhilosophyListView

urlpatterns = [
    path('', PhilosophyListView.as_view()),
]