from django.urls import path
from . import views

urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
    path('addProduct',views.addProduct,name='addProduct'),
    path('removeProduct',views.removeProduct,name='removeProduct'),
]