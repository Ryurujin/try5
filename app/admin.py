from django.contrib import admin
from .models import *


#user
@admin.register(ModelsUser)
class UserAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')
    #ordering = ('title')

#project
@admin.register(ProjectModels)
class ProjectAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')
    #ordering = ('title')

#task
@admin.register(TaskModels)
class TaskAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')
    #ordering = ('title')
