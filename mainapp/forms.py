from django import forms
from .models import App, Review, Category
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory


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


class PurchasePeriodForm(forms.Form):
    date_from = forms.DateField(
        label='С',
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
    )
    date_to = forms.DateField(
        label='По',
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
    )
    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')
        if date_from and date_to and date_from > date_to:
            raise forms.ValidationError(
                'Дата «С» не может быть позже даты «По».'
            )
        return cleaned_data


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


CategoryFormSet = modelformset_factory(
    Category,
    form=CategoryEditForm,
    extra=0,
)


class PriceFilterForm(forms.Form):
    price_min = forms.DecimalField(
        label='Цена от',
        required=False,
        min_value=0,
    )
    price_max = forms.DecimalField(
        label='до',
        required=False,
        min_value=0,
    )
    SORT_CHOICES = [
        ('', 'Порядок'),
        ('price', 'Сначала дешёвые'),
        ('-price', 'Сначала дорогие'),
        ('name', 'По названию'),
    ]
    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
    )
    def clean(self):
        cleaned_data = super().clean()
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')
        if (
            price_min is not None
            and price_max is not None
            and price_min > price_max
        ):
            raise forms.ValidationError(
                'Цена «от» не может быть больше цены «до».'
            )
        return cleaned_data