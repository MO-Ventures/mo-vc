import email
import io
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from apply.forms import (
    FILESIZE_LIMIT,
    SUPPORTED_FORMAT,
    FundingApplicationForm,
    PartnershipForm,
)
from django.template.loader import render_to_string
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from movc.settings import config

def send_email(subject, body, file):
    message = MIMEMultipart()
    message["From"] = config['email']['account']['email']
    message["To"] = ', '.join(config['email']['recipient'])
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    if file:
        part = MIMEBase("application", "octet-stream")
        attachment = io.BytesIO(file.read())
        part.set_payload(attachment.read())
        attachment.close()
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f'attachment; filename= {file}',
        )
        message.attach(part)    

    context = ssl.create_default_context()
    with smtplib.SMTP(config['email']['account']['smtp_server'], config['email']['account']['port']) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(config['email']['account']['email'], config['email']['account']['password'])
        server.sendmail(config['email']['account']['email'], message["To"], message.as_string())

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
        html = render_to_string(
            'apply/email.html', 
            context=dict(
                category='협력/제휴 제안서',
                contents=[
                    f'이름: {form.cleaned_data["name"]}',
                    f'회사: {form.cleaned_data["company"]}',
                    f'이메일: {form.cleaned_data["email"]}',
                    f'휴대폰번호: {form.cleaned_data["phone_number"]}',
                    f'제목: {form.cleaned_data["title"]}',
                    f'내용:<br/>{form.cleaned_data["message"]}',
                ]
            )
        ) 
        send_email(f'[첨부] 협력/제휴 제안서', html, form.cleaned_data["file"])
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
        html = render_to_string(
            'apply/email.html', 
            context=dict(
                category='투자 제안서',
                contents=[
                    f'이름: {form.cleaned_data["name"]}',
                    f'회사: {form.cleaned_data["company"]}',
                    f'이메일: {form.cleaned_data["email"]}',
                    f'휴대폰번호: {form.cleaned_data["phone_number"]}',
                    f'회사에 대해 간략한 소개:<br/>{form.cleaned_data["about_company"]}',
                    f'투자금 활용 방안:<br/>{form.cleaned_data["about_fund"]}',
                    f'회수 전략:<br/>{form.cleaned_data["exit_strategy"]}',
                ]
            )
        ) 
        send_email(f'[첨부] 투자 제안서', html, form.cleaned_data["file"])
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'apply/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'text-black'
        return context