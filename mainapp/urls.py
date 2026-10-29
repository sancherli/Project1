from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

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
    path('app/<int:app_id>/favorite/',views.toggle_favorite,name='toggle_favorite'),
    path('category/<int:category_id>/<str:category_name>/',views.category_detail,name='category_detail'),

    path('api/app/<int:id>/',views.api_app_detail,name='api_app_detail'),
    path('cheap/', views.index,{'max_price': 10},name='cheap'),
    path('premium/',views.index,{'min_price': 15},name='premium'),

    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.StoreLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('my-apps/',views.my_apps,name='my_apps'),

    path('favorites/',views.favorites,name='favorites'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='mainapp/password_reset_form.html',email_template_name='mainapp/password_reset_email.html',subject_template_name='mainapp/password_reset_subject.txt',success_url=reverse_lazy('mainapp:password_reset_done'),),name='password_reset',),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='mainapp/password_reset_done.html',),name='password_reset_done',),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='mainapp/password_reset_confirm.html',success_url=reverse_lazy('mainapp:password_reset_complete'),),name='password_reset_confirm',),

    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='mainapp/password_reset_complete.html',),name='password_reset_complete',),

    path('bulk-discount/',views.bulk_discount,name='bulk_discount',),

    path('category/<int:category_id>/merge/',views.merge_category,name='merge_category',),

    path('my-purchases/',views.my_purchases,name='my_purchases',),
    path('app/<int:app_id>/review/', views.add_review,name='add_review',),
    path('app/<int:app_id>/edit/',views.edit_apps,name='edit_app',),
    path('app/<int:app_id>/favorite/',views.toggle_favorite,name='toggle_favorite',),
    path('app/<int:app_id>/purchase/',views.buy_app,name='buy_app',),

    path('app/<int:app_id>/<str:app_name>/',views.AppDetailView.as_view(),name='app_detail',),
]

