from django.contrib import admin
from .models import Project, Task

# permitir ver campos de solo lectura en el panel
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Project)
admin.site.register(Task,TaskAdmin)
