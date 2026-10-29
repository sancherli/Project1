from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AppQuerySet(models.QuerySet):
    def free(self):
        return self.filter(price=0)

    def paid(self):
        return self.filter(price__gt=0)


class App(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(
                0,
                message='Цена не может быть отрицательной.'
            ),
        ],
    )
    objects = models.Manager.from_queryset(AppQuerySet)()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='apps',
    )
    rating_avg = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        editable=False,
    )

    rating_count = models.PositiveIntegerField(
        default=0,
        editable=False,
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
    favorited_by = models.ManyToManyField(
        User,
        related_name='favorite_apps',
        blank=True,
    )
    buyers = models.ManyToManyField(
        User,
        through='Purchase',
        related_name='purchased_apps',
        blank=True,
    )
    def get_absolute_url(self):
        return reverse(
            'mainapp:app_detail',
            kwargs={
                'app_id': self.id,
                'app_name': self.name,
            }
        )
    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        related_name='purchases',
    )
    paid_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    purchased_at = models.DateTimeField(
        auto_now_add=True,
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'app'],
                name='unique_user_app_purchase',
            ),
        ]
    def __str__(self):
        return f'{self.user.username} — {self.app.name}'

    def get_absolute_url(self):
        return reverse(
            'mainapp:app_detail',
            kwargs={
                'app_id': self.id,
                'app_name': self.name,
            }
        )
    def get_price_label(self):
        if self.price == 0:
            return 'Бесплатно'
        return f'{self.price} $'


class Review(models.Model):
    name = models.CharField(max_length=100)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    comment = models.TextField()
    text = models.TextField()
    recommended = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                1,
                message='Оценка не может быть меньше 1.'
            ),
            MaxValueValidator(
                5,
                message='Оценка не может быть больше 5.'
            ),
        ],
    )

    def __str__(self):
        return f"{self.name} → {self.app.name}"

# Create your models here.
