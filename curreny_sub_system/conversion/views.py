from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CurrencyConversion
from .serializers import CurrencyConversionSerializer
from decimal import Decimal
import datetime
import requests


def get_latest_exchange_rate(source_currency, target_currency):
    
    # # too slow and not availble #
    # # Use forex-python to fetch real-time exchange rate and perform conversion
    # currency_rates = CurrencyRates()
    # # target_amount = c.convert(source_currency, target_currency,source_amount)
    # conversion_rate = currency_rates.get_rate(source_currency, target_currency)
    
    # faster library for real-time exchange but uses API key
    # Use forex-python to fetch real-time exchange rate and perform conversion
    response = requests.get(f"https://v6.exchangerate-api.com/v6/479d6ca66f937907fee55fc3/pair/{source_currency}/{target_currency}") 
    
    return  Decimal(response.json()["conversion_rate"])


class CurrencyConversionAPIView(APIView):
    def post(self, request, format=None):
        serializer = CurrencyConversionSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            source_currency = serializer.validated_data['from_currency']
            target_currency = serializer.validated_data['to_currency']
            source_amount = serializer.validated_data['amount']

            conversion_rate = get_latest_exchange_rate(source_currency, target_currency)
            target_amount = source_amount * conversion_rate

            # Save the conversion result in the database
            conversion = CurrencyConversion.objects.create(
                user = user,
                from_currency = source_currency,
                to_currency = target_currency,
                amount = target_amount,
                conversion_rate = conversion_rate,
                created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            serialized_response = CurrencyConversionSerializer(conversion)

            return Response(serialized_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryAPIView(APIView):
    def get(self, request, format=None):
        user = request.user
        if user:
           
            # Save the conversion result in the database
            conversion = CurrencyConversion.objects.filter(user=user)
            serialized_response = CurrencyConversionSerializer(conversion, many=True)

            return Response(serialized_response.data, status=status.HTTP_201_CREATED)
            
        return Response({'error': 'User not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)