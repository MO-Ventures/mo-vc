from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home/index.html")),
    path('robots.txt/', TemplateView.as_view(template_name="home/robots.txt", content_type="text/plain")),
]