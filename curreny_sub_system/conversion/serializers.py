from rest_framework import serializers
from .models import CurrencyConversion, ConversionRate

class ConversionRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionRate
        fields = '__all__'

class CurrencyConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversion
        exclude = ['user']


