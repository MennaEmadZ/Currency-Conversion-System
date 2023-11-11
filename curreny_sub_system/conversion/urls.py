from django.urls import path
from .views import CurrencyConversionAPIView, HistoryAPIView

urlpatterns = [
    path('conversion/', CurrencyConversionAPIView.as_view(), name='currency-conversions'),
    path('history/', HistoryAPIView.as_view(), name='conversion-history'),
]