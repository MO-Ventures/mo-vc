from typing import List

from apply.forms import (
    FILESIZE_LIMIT,
    SUPPORTED_FORMAT,
    FundingApplicationForm,
    PartnershipForm,
)
from apply.templates import funding_message, partnership_message
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from movc.settings import config
from slack import WebClient

client = WebClient(token=config['slack']['token'])

# Create your views here.
class PartnershipFormView(FormView):
    template_name = 'apply/partnership.html'
    form_class = PartnershipForm
    success_url = '/apply/success'

    def get_context_data(self, **kwargs):
        if translation.get_language() == 'ko':
            PartnershipFormView.success_url = '/ko/apply/success'
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        context['upload_config'] = {
            'supported_format': SUPPORTED_FORMAT,
            'unsupported_format_error': _('File Not Supported'),
            'maximum_size': FILESIZE_LIMIT,
            'maximum_size_error': _('The file is too large. Must be less than 20mb'),
        }
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        client.chat_postMessage(
            channel=config['slack']['channel'],
            blocks=partnership_message(
                f'{form.cleaned_data["company"]} 업무 제휴 제안서',
                form.cleaned_data['name'],
                form.cleaned_data['company'],
                form.cleaned_data['email'],
                form.cleaned_data['phone_number'],
                form.cleaned_data['title'],
                form.cleaned_data['message'],
            )
        )
        if form.cleaned_data['file']:
            client.files_upload(
                channels=config['slack']['channel'],
                file=form.cleaned_data['file'],
                title=f'{form.cleaned_data["company"]}_자료'
            )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class FundingApplicationFormView(FormView):
    template_name = 'apply/investment.html'
    form_class = FundingApplicationForm
    success_url = '/apply/success'

    def get_context_data(self, **kwargs):
        if translation.get_language() == 'ko':
            FundingApplicationFormView.success_url = '/ko/apply/success'
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context
    
    def form_valid(self, form):
        client.chat_postMessage(
            channel=config['slack']['channel'],
            blocks=funding_message(
                f'{form.cleaned_data["company"]} 투자 제안서',
                form.cleaned_data['name'],
                form.cleaned_data['company'],
                form.cleaned_data['email'],
                form.cleaned_data['phone_number'],
                form.cleaned_data['about_company'],
                form.cleaned_data['about_fund'],
                form.cleaned_data['exit_strategy'],
            )
        )
        client.files_upload(
            channels=config['slack']['channel'],
            file=form.cleaned_data['file'],
            title=f'{form.cleaned_data["company"]}_IR_자료'
        )
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'apply/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context