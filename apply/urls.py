from apply.views import FundingApplicationFormView, PartnershipFormView, SuccessView
from django.urls import path

urlpatterns = [
    path('partnership/', PartnershipFormView.as_view()),
    path('investment/', FundingApplicationFormView.as_view()),
    path('success/', SuccessView.as_view()),
]