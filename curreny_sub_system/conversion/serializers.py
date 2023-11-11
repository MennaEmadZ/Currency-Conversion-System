from rest_framework import serializers
from .models import CurrencyConversion


class CurrencyConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversion
        exclude = ['user']


