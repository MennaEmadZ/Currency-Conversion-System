from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import CurrencyConversion
from .views import CurrencyConversionAPIView, get_latest_exchange_rate
from .serializers import CurrencyConversionSerializer
from decimal import Decimal
from unittest.mock import patch
