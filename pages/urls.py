from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home-page'),
    path('about',views.about,name='about-page'),
    path('contact',views.contact,name='contact-page'),
    path('login',views.login,name='login-page'),
    path('logout',views.logout,name='logout-page'),
    path('login_process',views.login_process,name='login_process'),
]