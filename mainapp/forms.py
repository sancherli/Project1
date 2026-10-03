from django import forms
from .models import App, Review
from django.conf import settings


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
