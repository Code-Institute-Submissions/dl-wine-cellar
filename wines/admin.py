from django.contrib import admin
from .models import Wine, Category, Grape

# Register models here

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'product_code',
        'name',
        'country',
        'price',
        'category',
        'rating',
        'image',
    )

    ordering = ('product_code',)

class CategoryAdmin(admin.ModelAdmin):
        list_display = (
        'friendly_name',
        'name',
    )

class GrapeAdmin(admin.ModelAdmin):
        list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Wine, WineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Grape, GrapeAdmin)
