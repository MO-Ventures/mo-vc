from modeltranslation.translator import register, TranslationOptions
from portfolio.models import Company

@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name',)