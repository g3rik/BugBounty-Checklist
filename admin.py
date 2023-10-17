from django.contrib import admin
from .models import *

class MasterChecklistAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')  # Include 'topic' in the list display

class ResultAdmin(admin.ModelAdmin):
    list_display = ('website', 'checkpoint')

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(MasterChecklist, MasterChecklistAdmin)
# admin.site.register(ChecklistPoint)
admin.site.register(Result, ResultAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(MasterTopic)