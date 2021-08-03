from django.contrib import admin
from portfolio.models import Company, Statistics
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
    pass

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    pass