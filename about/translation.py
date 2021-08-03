from modeltranslation.translator import register, TranslationOptions
from philosophy.models import Philosophy

@register(Philosophy)
class PhilosophyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
