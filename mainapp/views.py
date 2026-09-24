from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from .models import App, Category, Review
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView, TemplateView, ListView


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


@require_GET
def api_app_detail(request, id):
    app = get_object_or_404(App, id=id)
    return JsonResponse({
        'id': app.id,
        'name': app.name,
        'description': app.description,
        'price': str(app.price),
        'icon': app.icon.url if app.icon else None,
    })


@require_GET
def index(request, max_price=None, min_price=None):
    apps = App.objects.all()
    if max_price is not None:
        apps = apps.filter(price__lte=max_price)
    elif min_price is not None:
        apps = apps.filter(price__gte=min_price)
    return render(request, 'mainapp/home.html', {
        'apps': apps,
    })


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'


class AppListView(ListView):
    model = App
    template_name = 'mainapp/home.html'
    context_object_name = 'apps'
    paginate_by = 2
    ordering = 'id'


class AppDetailView(DetailView):
    model = App
    template_name = 'mainapp/app_detail.html'
    context_object_name = 'app'
    pk_url_kwarg = 'app_id'

# Create your views here.
