from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Categories, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'availability', ]
    list_filter = ['availability', 'category']
    list_editable = ['price', 'availability']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)
