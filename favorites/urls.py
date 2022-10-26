from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path('products/', include('products.urls')),
]