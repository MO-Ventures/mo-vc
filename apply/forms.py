from django import forms
from django.core.exceptions import ValidationError

FILESIZE_LIMIT = 20 * 1000 * 1000 # 20mb
SUPPORTED_FORMAT = ['pdf', 'docx', 'doc', 'ppt', 'pptx', 'hwp', 'zip']

def validate_file_size(file):
    if file.size > FILESIZE_LIMIT:
        raise ValidationError('Too big. Must be 20mb')

def validate_file_format(file):
    if not file.name.split('.')[-1] in SUPPORTED_FORMAT:
        raise ValidationError(f'Unsupported Format. Must be f{", ".join(SUPPORTED_FORMAT)}')

class PartnershipForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    company = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    title = forms.CharField(max_length=200, required=True)
    message = forms.CharField(max_length=2000, required=True)
    file = forms.FileField(
        required=False, 
        validators=[
            validate_file_size,
            validate_file_format,
            ]
        )

class FundingApplicationForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    company = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    about_company = forms.CharField(max_length=2000, required=True)
    about_fund = forms.CharField(max_length=2000, required=True)
    exit_strategy = forms.CharField(max_length=2000, required=True)
    file = forms.FileField(
        required=True, 
        validators=[
            validate_file_size,
            validate_file_format,
            ]
        )