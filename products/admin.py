from django.contrib import admin
from .models import Product, Category, PositiveReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class PositiveReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'product', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


admin.site.register(PositiveReview,PositiveReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
