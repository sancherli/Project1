from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} → {self.app.name}"

# Create your models here.
