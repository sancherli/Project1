from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from Project1")

# Create your views here.
