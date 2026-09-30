from django.db.models import Count
from .models import Category


def store_menu(request):
    nav_categories = (
        Category.objects
        .annotate(apps_count=Count('apps'))
        .order_by('name')
    )
    return {
        'nav_categories': nav_categories,
    }
