from django.shortcuts import render
from .models import App, Review


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

# Create your views here.
