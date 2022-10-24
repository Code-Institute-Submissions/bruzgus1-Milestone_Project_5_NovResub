from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('positive_reviews/<product_id>', views.positive_reviews_view, name='positive_reviews'),
    path('negative_reviews/<product_id>', views.negative_reviews_view, name='negative_reviews'),
]
