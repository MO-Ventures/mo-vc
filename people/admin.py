from adminsortable.admin import SortableAdmin
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from people.models import People

# Register your models here.
@admin.register(People)
class PeopleAdmin(SortableAdmin, TranslationAdmin):
    pass