from modeltranslation.translator import register, TranslationOptions
from people.models import People

@register(People)
class PeopleTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description',)