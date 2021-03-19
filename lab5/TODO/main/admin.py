from django.contrib import admin
from main.models import *


admin.site.register(List)
admin.site.register(Person)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ['task']
    search_fields = ['task']
    list_filter = ['created', 'due_on', ]
