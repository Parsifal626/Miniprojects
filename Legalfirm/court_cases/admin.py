from django.contrib import admin
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'case_title', 'date_filed', 'court')
    list_filter = ('court',)
    search_fields = ('case_number', 'case_title')
