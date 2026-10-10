from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='apps',
    )
    icon = models.ImageField(
        upload_to='icons/',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='apps',
    )

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    text = models.TextField()
    recommended = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.app.name}"

# Create your models here.
