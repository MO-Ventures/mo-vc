from modeltranslation.translator import register, TranslationOptions
from people.models import Introduction, People

@register(Introduction)
class IntroductionTranslationOptions(TranslationOptions):
    fields = ('heading', 'subheading',)

@register(People)
class PeopleTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description',)