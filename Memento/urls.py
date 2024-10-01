from django.contrib import admin
from django.urls import path
from . import views  # Assurez-vous que cela est correct

urlpatterns = [

    path('Memenfos', views.Mori, name='Mori'),
    path('', views.Memenfos, name='Memenfos'),
    path('Moria', views.Moria, name='Moria'),
    path('signup', views.signup_view, name='signup'),
    path('compteur/', views.show_counter, name='show_counter'),

   
]
