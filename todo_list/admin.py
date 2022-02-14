from django.contrib import admin

# Register your models here.
from todo_list.models import Task

admin.site.register(Task)