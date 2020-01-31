from django.contrib import admin
from .models import Editor,images,tags

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(images,ImagesAdmin)
admin.site.register(tags)
