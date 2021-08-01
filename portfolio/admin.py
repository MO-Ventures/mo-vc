from django.contrib import admin
from portfolio.models import Company, Statistics

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    pass