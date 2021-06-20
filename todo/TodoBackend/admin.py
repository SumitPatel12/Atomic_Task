from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title_id", "title", "description", "status")


#? Register to Admin Site ?#
admin.site.register(Todo, TodoAdmin)
