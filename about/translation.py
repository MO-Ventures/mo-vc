from modeltranslation.translator import register, TranslationOptions
from about.models import Philosophy

@register(Philosophy)
class PhilosophyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
