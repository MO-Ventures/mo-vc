from adminsortable.admin import SortableAdmin
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from people.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(SortableAdmin, TranslationAdmin):
    pass