from django import forms
from .models import App, Review
from django.conf import settings
from django import forms
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
        ]


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(
        label='Электронная почта',
        required=True
    )
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
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Пользователь с такой электронной почтой уже существует.'
            )

        return email


