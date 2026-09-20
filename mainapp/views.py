from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import App, Category, Review
from django.core.paginator import Paginator
from django.db.models import Q

def about(request):
    return render(request, 'mainapp/about.html')


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'mainapp/reviews.html', {
        'reviews': reviews
    })

@require_POST
def add_review(request, app_id):
    app = get_object_or_404(App, id=app_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.app = app
        review.save()
        return redirect('main:app_detail', app_id=app.id)


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

def app_detail(request, app_id, app_name):
    print(app_name)
    app = get_object_or_404(App, id=app_id)
    return render(request, 'mainapp/app_detail.html', {
        'app': app,
    })

def category_detail(request, category_id, category_name):
    print(category_name)
    category = get_object_or_404(Category, id=category_id)
    apps = App.objects.filter(category=category)
    paginator = Paginator(apps, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    most_expensive = apps.order_by('-price').first()
    return render(request, 'mainapp/category.html', {
        'category': category,
        'apps': page_obj,
        'page_obj': page_obj,
        'most_expensive': most_expensive,
    })

def home(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    apps = App.objects.all()
    if q:
        apps = apps.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q)
        ).order_by('name')
    else:
        apps = apps.order_by('-created_at')
    paginator = Paginator(apps, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    app_of_day = App.objects.order_by('-price').first()
    return render(request, 'mainapp/home.html', {
        'apps': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'app_of_day': app_of_day,
        'q': q,
        'sort': sort,
    })


def new(request):
    apps = App.objects.order_by('-created_at')
    paginator = Paginator(apps, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mainapp/new.html', {
        'apps': page_obj,
        'page_obj': page_obj,
    })

# Create your views here.
