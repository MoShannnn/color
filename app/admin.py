from django.contrib import admin
from app.models import Color, Category, Season
# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex', 'category', 'season')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Color, ColorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Season, SeasonAdmin)
