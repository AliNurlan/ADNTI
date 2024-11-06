from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'salary')
    search_fields = ('full_name', 'position')
    list_filter = ('position',)
