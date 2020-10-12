from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'manager']
    list_filter = ['id', 'first_name','manager']
    search_fields = ['first_name','manager']