from modeltranslation.translator import register, TranslationOptions
from people.models import Employee

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description',)