from django import template

register = template.Library()


@register.filter
def stars(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return ''

    return '★' * value + '☆' * (5 - value)


@register.filter
def reviews_count(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return '0 отзывов'

    last_two = value % 100
    last_one = value % 10

    if 11 <= last_two <= 14:
        word = 'отзывов'
    elif last_one == 1:
        word = 'отзыв'
    elif last_one in (2, 3, 4):
        word = 'отзыва'
    else:
        word = 'отзывов'

    return f'{value} {word}'