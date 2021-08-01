from django.urls import path
from portfolio.views import CompanyListView

urlpatterns = [
    path('', CompanyListView.as_view()),
]