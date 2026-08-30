from django.contrib import admin
from .models import App, Category, Review


admin.site.register(App)
admin.site.register(Category)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'app')
# Register your models here.
