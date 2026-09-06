from django.shortcuts import render, get_object_or_404
from .models import App, Category, Review


def home(request):
    apps = App.objects.all()
    app_of_day = App.objects.order_by('-price').first()
    return render(request, 'mainapp/home.html', {
        'apps': apps,
        'app_of_day': app_of_day,
    })


def about(request):
    return render(request, 'mainapp/about.html')


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'mainapp/reviews.html', {
        'reviews': reviews
    })


def free_apps(request):
    apps = App.objects.filter(price=0)
    return render(request, 'mainapp/free.html', {
        'apps': apps
    })

def top_apps(request):
    apps = App.objects.filter(price__gt=0).order_by('-price')[:10]
    return render(request, 'mainapp/top.html', {
        'apps': apps
    })

def app_detail(request, app_id):
    app = get_object_or_404(App, id=app_id)

    return render(request, 'mainapp/app_detail.html', {
        'app': app
    })


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    apps = App.objects.filter(category=category)
    most_expensive = apps.order_by('-price').first()

    return render(request, 'mainapp/category.html', {
        'category': category,
        'apps': apps,
        'most_expensive': most_expensive,
    })


def home(request):
    apps = App.objects.all()
    categories = Category.objects.all()
    app_of_day = App.objects.order_by('-price').first()

    return render(request, 'mainapp/home.html', {
        'apps': apps,
        'categories': categories,
        'app_of_day': app_of_day,
    })

# Create your views here.
