from django import forms
from .models import Review


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