from django import forms
from .models import App, Review
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'name',
            'rating',
            'comment',
            'recommended',
        ]

        labels = {
            'name': 'Имя',
            'rating': 'Оценка',
            'comment': 'Комментарий',
            'recommended': 'Рекомендуете приложение?',
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                'Оценка должна быть от 1 до 5.'
            )
        return rating


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = [
            'name',
            'description',
            'price',
            'category',
            'icon',
        ]


class ForSuperUserEditAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = [
            'name',
            'description',
            'price',
            'category',
            'icon',
            'author',
        ]


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']