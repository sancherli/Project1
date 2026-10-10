from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'mainapp'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('free/', views.free_apps, name='free'),
    path('top/', views.top_apps, name='top'),
    path('new/', views.new, name='new'),
    path('', views.AppListView.as_view(), name='home'),

    path('app/<int:app_id>/review/', views.add_review, name='add_review'),
    path('app/<int:app_id>/edit/',views.edit_apps,name='edit_app'),
    path('app/<int:app_id>/<str:app_name>/',views.AppDetailView.as_view(),name='app_detail'),
    path('category/<int:category_id>/<str:category_name>/',views.category_detail,name='category_detail'),

    path('api/app/<int:id>/',views.api_app_detail,name='api_app_detail'),
    path('cheap/', views.index,{'max_price': 10},name='cheap'),
    path('premium/',views.index,{'min_price': 15},name='premium'),

    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.StoreLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('my-apps/',views.my_apps,name='my_apps'),
]
