from django.contrib import admin
from .models import Product, Category, PositiveReview, NegativeReview

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
    list_display = ('name', 'positive_review', 'product', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'positive_review')


class NegativeReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'negative_review', 'product', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'negative_review')


admin.site.register(NegativeReview, NegativeReviewAdmin)
admin.site.register(PositiveReview, PositiveReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
