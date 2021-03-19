from django.contrib import admin
from .models import Bb
class BbAdmin(admin.ModelAdmin):
    list_display = ("title", 'description', 'price', 'priceSymbol', 'data')
    list_display_links = ("title",)
    search_fields = ("title",)
admin.site.register(Bb, BbAdmin)
