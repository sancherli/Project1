from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('free/', views.free_apps, name='free'),
    path('top/', views.top_apps, name='top'),
    path('new/', views.new, name='new'),

    path('app/<int:app_id>/<str:app_name>/',views.app_detail,name='app_detail'),
    path('category/<int:category_id>/<str:category_name>/',views.category_detail,name='category_detail'),
]
