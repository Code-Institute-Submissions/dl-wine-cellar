from django.contrib import admin
from .models import Wine, Category, Grape

# Register models here
admin.site.register(Wine)
admin.site.register(Category)
admin.site.register(Grape)
