from django.urls import path
from about.views import BusinessModelView, PhilosophyView

urlpatterns = [
    path('', BusinessModelView.as_view()),
    path('business_model/', BusinessModelView.as_view()),
    path('philosophy/', PhilosophyView.as_view()),
]