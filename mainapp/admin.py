from django.contrib import admin
from .models import App, Category, Review, Purchase

admin.site.register(App)
admin.site.register(Category)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'app')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'app',
        'paid_price',
        'purchased_at',
    )
# Register your models here.

