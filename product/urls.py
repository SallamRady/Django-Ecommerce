from django.urls import path
from . import views

urlpatterns = [
    path('',views.listAll,name='product-list'),
    path('<int:id>',views.product,name='product-details'),
    path('category/<int:id>',views.category,name='category-products'),
]