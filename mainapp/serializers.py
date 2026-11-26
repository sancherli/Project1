from rest_framework import serializers
from .models import App, Review


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='name',
        read_only=True,
    )
    stars = serializers.IntegerField(
        source='rating',
    )
    class Meta:
        model = Review
        fields = [
            'id',
            'username',
            'stars',
            'comment',
            'recommended',
            'created_at',
        ]
        read_only_fields = ['username', 'created_at']