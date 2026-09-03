from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('free/', views.free_apps, name='free'),
    path('top/', views.top_apps, name='top'),
]
