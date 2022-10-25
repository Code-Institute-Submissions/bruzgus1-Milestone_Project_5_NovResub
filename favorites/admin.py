from django.contrib import admin
from .models import Favorite

# Register your models here.


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )

admin.site.register(Favorite, FavoriteAdmin)