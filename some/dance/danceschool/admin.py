from django.contrib import admin
from .models import *


class ProflieAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'rang', 'category')


admin.site.register(Profile, ProflieAdmin)
admin.site.register(Post)
admin.site.register(Commands)
admin.site.register(Achievements)
admin.site.register(Tree)
# admin.site.register(Messenger)


