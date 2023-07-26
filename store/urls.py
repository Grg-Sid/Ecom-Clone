from django.urls import path, reverse
from . import views

# URL Routes
urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>", views.product_detail),
    path("collections/", views.collection_list),
    path("collections/<int:pk>", views.collection_detail, name="collection-detail"),
]
