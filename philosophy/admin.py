from django.contrib import admin
from philosophy.models import Philosophy
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Philosophy)
class PhilosophyAdmin(TranslationAdmin):
    pass